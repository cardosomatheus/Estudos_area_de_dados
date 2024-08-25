from mysql.connector import connect
from configuracao import nova_conexao


with nova_conexao() as conexao:
    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute('SHOW DATABASES')
       
        for i, database in enumerate(cursor, start=1):
            print(f'Base de dados {i}: {database[0]}')
