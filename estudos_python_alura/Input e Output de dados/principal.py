import contato_utils 

# retorna a leitura dos dados
contatos = contato_utils.csv_para_contatos('contatos.csv','latin_1')

# converte para pickle (binario) e  faz a leitura
contato_utils.contatos_para_pickle(contatos,'contatos.pickle')  
contatos  = contato_utils.pickle_para_contatos(caminho='contatos.pickle')


# converte para json e  faz a leitura
contato_utils.contatos_para_json(contatos,'contatos.json')
contatos = contato_utils.json_para_contato('contatos.json')

for contato in contatos:
    print(contato.id, contato.nome, contato.email)


