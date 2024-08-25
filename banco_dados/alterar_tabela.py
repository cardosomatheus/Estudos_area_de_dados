from configuracao import nova_conexao


sql_alter = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_alter)
    except Exception as e:
        print(e)