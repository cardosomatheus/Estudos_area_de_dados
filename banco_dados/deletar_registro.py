from configuracao import nova_conexao
from mysql.connector.errors import ProgrammingError

# Consulta limitada de registros
delete_filtrado = """DELETE FROM CONTATOS WHERE NOME LIKE %s"""
with nova_conexao() as conexao: 
    nome_like = input('Pesquisa por nome: ')
    args = (f'%{nome_like}%',)
    
    try:
        cursor = conexao.cursor()
        cursor.execute(delete_filtrado, args)
        conexao.commit() 
    except ProgrammingError as e: 
        print(e.msg)
        
    else:
        print('registros deletados:', cursor.rowcount)