
def imc_body(peso, altura_metros):
    imc = round(peso / (altura_metros * altura_metros), 2)
    print('IMC:', imc)


def bigger_value(valor_1, valor_2):
    if valor_1 > valor_2:
        print('maior valor:', valor_1)
    elif valor_1 == valor_2:
        print('valores iguais:', valor_1, ' =', valor_2)
    elif valor_1 < valor_2:
        print('maior valor:', valor_2)
    else:
        print('nda')


def name_age(nome, idade):

    if ' ' in nome:
        vespacos = 'contem espacos'
    else:
        vespacos = 'não contem espacos'

    if nome and idade is not None:
        print('Nome:', nome)
        print('Nome invertido:', nome[::-1])
        print('O seus nome', vespacos)
        print('Primeira letra:', nome[0])
        print('Ultima letra:', nome[-1])
    else:
        print('Campos Vazios')
