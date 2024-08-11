# Conceito de funções de primeira classe.

def dobro(x):
    return x *2

def quadrado(x):
    return x**4


if __name__ == '__main__':
    lista_funcoes = [dobro,quadrado ] * 5
    for function, numero in zip(lista_funcoes, range(1,11)):
    
        #print(f'{numero}',end=' ')      
        print(f'O {function.__name__} de {numero} é:  {function(numero)}')