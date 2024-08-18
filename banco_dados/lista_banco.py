from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='mcds123'
)

cursor2 = conexao.cursor()
databases = cursor2.execute('SHOW DATABASES')


for i, database in enumerate(cursor2, start=1):
    print(f'Base de dados {i}: {database[0]}')
