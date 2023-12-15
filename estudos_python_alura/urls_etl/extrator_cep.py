import re
endereco="rua das flores  72, apartamento 1002, Rio de Janeiro, 25540-105"



padrao =re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)