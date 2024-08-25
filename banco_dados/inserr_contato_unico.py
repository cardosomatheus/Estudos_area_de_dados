from configuracao import nova_conexao


sql_inserir_contato = 'INSERT INTO CONTATOS (NOME,TEL) VALUES (%s,%s)'
args = ('JOSE', '99999-9999')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_inserir_contato,args)
        conexao.commit()
        print('Inserção feita. Linha', cursor.lastrowid)
    except Exception as e:
        print(e)