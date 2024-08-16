from functools import reduce

def fatorial_funcional(n):
    lista_de_valores  = list(range(1,(n)))
    return reduce(lambda  fatorial, x : x * fatorial, lista_de_valores,n) if n > 1 else 1

def fatorial_recursivo(n):
    return n * fatorial_recursivo(n-1) if n > 1 else 1


if __name__ == '__main__':
    print(f'funcional: 0!:  {fatorial_funcional(0)} recursivo: 10!:  {fatorial_recursivo(0)}')   
    print(f'funcional: 1!:  {fatorial_funcional(1)} recursivo: 10!:  {fatorial_recursivo(1)}')   
    print(f'funcional: 5!:  {fatorial_funcional(5)} recursivo: 10!:  {fatorial_recursivo(5)}')   
    print(f'funcional: 10!:  {fatorial_funcional(10)} recursivo: 10!:  {fatorial_recursivo(10)}')

