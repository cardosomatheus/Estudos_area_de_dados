from configuracao import nova_conexao


sql_inserir_contato = 'INSERT INTO CONTATOS (NOME,TEL) VALUES (%s,%s)'
args = (
    ('Ana', '96765-4321'),
    ('Bia', '97765-4321'),
    ('Luca', '89765-4321'),
    ('Lu', '98765-4321'),
    ('Gui', '98735-4321'),
    ('Beca', '98765-2221'),
    ('Pedro', '98765-6721'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql_inserir_contato,args)
        conexao.commit()
        print('Inserção feita. qtd de retgistros: ', cursor.rowcount)
    except Exception as e:
        print(e)
        
        
