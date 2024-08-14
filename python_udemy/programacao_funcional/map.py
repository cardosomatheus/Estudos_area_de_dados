if __name__ == '__main__':
    lista_1 = [1,2,5,8]
    dobro = list(map(lambda x: x*2, lista_1))
    print(dobro)
    
    nomes  = (
    {'NOME': 'Matheus', 'SOBRENOME':'Santos', 'IDADE' : 23},
    {'NOME': 'Jose', 'SOBRENOME':'Silva', 'IDADE' : 35},
    {'NOME': 'Sergio', 'SOBRENOME':'Alvez', 'IDADE' : 70},
    {'NOME': 'Claudio','SOBRENOME':'Perez', 'IDADE' : 50}
)

    primeiro_nome = list(map(lambda x: x['NOME'], nomes ))
    sobrenome     = list(map(lambda x: x['SOBRENOME'], nomes))
    idade_por_pessoas = map(lambda x: f'<{x["NOME"]}> tem <{x["IDADE"]}> anos.', nomes)
    print(f'First names: {primeiro_nome}')
    print()
    print(f'Last names: {sobrenome}')
    print()
    print(f'Idade: {list(idade_por_pessoas)}')