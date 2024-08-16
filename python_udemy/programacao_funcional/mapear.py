
def mapear_1(funcao, lista):
    for valor in lista:
        yield funcao(valor)


def mapear_2(funcao, lista):
    return (funcao(valor) for valor in lista)


if __name__ == '__main__':
    print(list(mapear_1(lambda x: x ** 2 , [2,3,4])))

    print(list(mapear_2(lambda x: x ** 2 , [2,3,4])))