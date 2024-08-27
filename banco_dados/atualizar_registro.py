from configuracao import nova_conexao
from mysql.connector.errors import ProgrammingError

# Consulta limitada de registros
update_filtrado = """UPDATE CONTATOS
                        SET  NOME = %s
                       WHERE ID = %s"""
with nova_conexao() as conexao: 
    id_atualizar = input('Informe o id: ')
    novo_nome = input('Novo nome: ')
    args = (novo_nome,id_atualizar,)
    
    try:
        cursor = conexao.cursor()
        cursor.execute(update_filtrado, args)
        conexao.commit() 
    except ProgrammingError as e: 
        print(e.msg)
        
    else:
        print('registros Atualizados:', cursor.rowcount)