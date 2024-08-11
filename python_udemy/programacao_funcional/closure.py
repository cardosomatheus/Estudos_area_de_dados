# Closure


def multiplicar(x):
    """    
    Quando atribuimos multiplicar(x) em uma variavel ,na verdade estamos atribuindo a função interna (caluclar(y))
    Logo y = Ao valor informado na definiçao da variavel usada na def multitplicar.
    """
    def calcular(y):
        return x+y 
    return calcular



if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    
    
    print(f'X 2 : {dobro(10)}')
    print(f'X 3 : {triplo(10)}')