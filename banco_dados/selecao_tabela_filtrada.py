from configuracao import nova_conexao
from mysql.connector.errors import ProgrammingError

# Consulta limitada de registros
sql_filtrado = """ SELECT * FROM CONTATOS WHERE NOME LIKE %s"""
with nova_conexao() as conexao: 
    nome_like = input('Pesquisa por nome: ')
    args = (f'%{nome_like}%',)
    
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_filtrado, args)
    
    except ProgrammingError as e:
        print(e.msg) 
    
    else:
        for contato in cursor.fetchall():
            print('\t'.join(str(campo) for campo in contato))