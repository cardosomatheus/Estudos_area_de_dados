import os
import sys
from time import time


os.environ["NLS_LANG"] = "BRAZILIAN PORTUGUESE_BRAZIL.UTF8"
os.environ['SHAPE_ENCODING'] = "utf-8"

from osgeo import ogr
import cx_Oracle


chunksize = 1000

data_types = {ogr.OFTInteger: "NUMBER",
              ogr.OFTIntegerList: None,
              ogr.OFTReal: "NUMBER",
              ogr.OFTRealList: None,
              ogr.OFTString: "VARCHAR2",
              ogr.OFTStringList: None,
              ogr.OFTWideString: None,
              ogr.OFTWideStringList: None,
              ogr.OFTBinary: None,
              ogr.OFTDate: "DATE",
              ogr.OFTTime: None,
              ogr.OFTDateTime: "DATE",
              ogr.OFTInteger64: "NUMBER",
              ogr.OFTInteger64List: None}

conn_str = input(
    "Input connection string (format USER/PASSWORD@HOST:PORT/INSTANCE):\n"
)
conn = cx_Oracle.connect(conn_str)

table_name = input("Input table name to be loaded:\n").upper()
cur_table_check = conn.cursor()
cur_table_check.execute("SELECT COUNT(*)\n"
                        "  FROM USER_TABLES\n"
                        " WHERE TABLE_NAME = :P_TABLE_NAME\n",
                        P_TABLE_NAME=table_name)
row = cur_table_check.fetchone()
cur_table_check.close()
if row[0] > 0:
    while True:
        print("The table {0} already exists,"
              " do you want to delete it? (Y/N)".format(table_name))
        flag_drop_table = input().upper()
        if flag_drop_table in ('Y', 'N'):
            break
    if flag_drop_table == 'Y':
        cur_drop_table = conn.cursor()
        cur_drop_table.execute("DROP TABLE " + table_name)
        cur_drop_table.close()
    else:
        print("Exiting process...")
        sys.exit(1)

file_name = input("Input the Shape file to be loaded:\n")
if not os.path.isfile(file_name):
    print("File doesn's exists! Exiting process...")
    sys.exit(1),
file = ogr.Open(file_name)

if file.GetLayerCount() == 1:
    layer = file.GetLayer(0)
else:
    layers = list()
    for i in range(file.GetLayerCount()):
        layers.append(file.GetLayer(i))
    print("The file has more than one layer!")
    while True:
        layer_name = input("Choose between " + str(layers) + ":\n")
        if layer_name in layers:
            break
    layer = file.GetLayerByName(layer_name)

spatialRef = layer.GetSpatialRef()
if spatialRef:
    epsg = spatialRef.GetAttrValue("AUTHORITY", 1)
    print("EPSG:{0} has detected!".format(epsg))
while True:
    srid = input("Input the Oracle SRID code:\n")
    cur_srid = conn.cursor()
    cur_srid.execute("SELECT COUNT(*)\n"
                     "  FROM MDSYS.CS_SRS\n"
                     " WHERE SRID = :P_SRID\n",
                     P_SRID=srid)
    qtde_srid = cur_srid.fetchone()
    cur_srid.close()
    if qtde_srid[0] == 0:
        print("{0} SRID code not found!\n".format(srid))
    else:
        break

# Create the table
fields = list()
for i in range(layer.GetLayerDefn().GetFieldCount()):
    fields.append(
        {
            "COLUMN_NAME": layer.GetLayerDefn().GetFieldDefn(i).GetName(),
            "DATA_TYPE": data_types[
                layer.GetLayerDefn().GetFieldDefn(i).GetType()
            ],
            "DATA_LENGTH": layer.GetLayerDefn().GetFieldDefn(i).GetWidth()
        }
    )

str_create = "CREATE TABLE {0}\n(".format(table_name)
for i, field in enumerate(fields):
    str_create += "{0} {1}".format(field["COLUMN_NAME"], field["DATA_TYPE"])
    if field["DATA_TYPE"] not in ("DATE"):
        str_create += "({0}),\n".format(field["DATA_LENGTH"])
    else:
        str_create += ",\n"
str_create += "GEOMETRY MDSYS.SDO_GEOMETRY)"

cur_create = conn.cursor()
cur_create.execute(str_create)
cur_create.close()

# Insert rows
str_insert = "INSERT INTO {0}(".format(table_name)
for i, field in enumerate(fields):
    str_insert += field["COLUMN_NAME"] + ","
str_insert += "GEOMETRY) VALUES("
for i in range(len(fields)):
    str_insert += ":" + fields[i]["COLUMN_NAME"] + ","
str_insert += "MDSYS.SDO_GEOMETRY(:{0}, {1}))".format("WKT", srid)

cur_insert = conn.cursor()
cur_insert.prepare(str_insert)
wkt = None

columns = tuple(field["COLUMN_NAME"] for field in fields)
rows = list()
j = 0
start_time = time()
feature_count = layer.GetFeatureCount()
for i in range(feature_count):
    if not wkt:
        wkt = cur_insert.var(cx_Oracle.CLOB,
                             arraysize=min(feature_count - j + 1, chunksize))
    feature = layer.GetFeature(i)
    wkt_text = feature.geometry().ExportToWkt()
    wkt.setvalue(j, wkt_text)
    values = feature.items().values()
    row = dict(zip(columns, values))
    row["WKT"] = wkt
    rows.append(row)

    j += 1
    if (j == chunksize) or (i == feature_count - 1):
        cur_insert.bindarraysize = len(rows)
        cur_insert.executemany(None, rows)
        conn.commit()
        rows_per_s = i / (time() - start_time)
        if rows_per_s == 0:
            rows_per_s = 1
        print(
            "{0} rows inserted - {1} rows/second"
            " - {2} seconds to finish".format(
                i + 1,
                int(rows_per_s),
                int((feature_count - i + 1) / rows_per_s)
            )
        )
        rows = list()
        j = 0
        wkt = None

print(
    "{0} rows were loaded successfully in {1} seconds!".format(
        feature_count,
        int(time() - start_time)
    )
)

cur_insert.close()
conn.close()
