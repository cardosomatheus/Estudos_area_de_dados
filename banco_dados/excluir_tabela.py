from configuracao import nova_conexao



with nova_conexao() as conexao:
    try:
       cursor =  conexao.cursor()
       cursor.execute('DROP TABLE IF EXISTS EMAILS')
    except Exception as e:
        print(f'ERROR : {e.msg}')