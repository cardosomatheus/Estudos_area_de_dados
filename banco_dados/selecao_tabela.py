from configuracao import nova_conexao
from mysql.connector.errors import ProgrammingError

# Consulta limitada de registros
sql_filtrado = """ SELECT * FROM CONTATOS LIMIT 10"""
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_filtrado)
    except ProgrammingError as e:
        print(e) 
    else:
        for contato in cursor.fetchall():
            print('\t'.join(str(campo) for campo in contato))


# Linha unica.
sql_linha_unica = """SELECT * FROM CONTATOS"""
with nova_conexao() as conexao:
    cursor = conexao.cursor(buffered=True)
    cursor.execute(sql_linha_unica)
    print(cursor.fetchone())

