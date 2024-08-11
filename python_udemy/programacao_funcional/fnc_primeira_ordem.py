# Funções de primeira ordem.

from fnc_primeira_classe import dobro, quadrado


def processar(titulo ,lista,function):
    print(f'processando o  {titulo} dos valores.')
    
    for valor in lista:
        print(f'{valor} => {function(valor)}')
    print()       
        

if __name__ == '__main__':
    processar(titulo='Dobro', lista=range(1,11), function=dobro)
    processar(titulo='Quadrado', lista=range(1,11), function=quadrado)