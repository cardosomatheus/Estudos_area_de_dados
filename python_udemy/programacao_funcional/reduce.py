from functools import reduce
nomes = (
    {'NOME': 'Matheus', 'SOBRENOME': 'Santos', 'IDADE': 23},
    {'NOME': 'Jose', 'SOBRENOME': 'Silva', 'IDADE': 35},
    {'NOME': 'Sergio', 'SOBRENOME': 'Alvez', 'IDADE': 15},
    {'NOME': 'Claudio', 'SOBRENOME': 'Perez', 'IDADE': 50}
)


if __name__ == '__main__':
    # Calculado idade dos adultos usando programação funcional
    apenas_idades = map(lambda x: x['IDADE'], nomes)
    idade_maiores_de_idade = filter(lambda x: x >= 18, apenas_idades)
    soma_idade_dos_adultos = reduce(lambda idade, x: x+idade, idade_maiores_de_idade, 0)
    print(soma_idade_dos_adultos)

    # Leitura complexa mas com mesmo resultado.
    soma_idade_dos_adultos_2 = reduce(lambda idade, x: x+idade,filter(lambda x: x >= 18,map(lambda x: x['IDADE'], nomes)), 0)
    print(soma_idade_dos_adultos_2)


