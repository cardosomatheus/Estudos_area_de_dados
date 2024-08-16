from math import gcd

# Forma mais simples, usandos um metodo pronto de uma pakcage.
def mcd_1(numeros):  
    return gcd(*numeros)


# Elaborada individualmente após tempo entendendo e colocando a mão na massa.
def mcd_2(numeros):
    maximo_divisor_comum = 0
    menor_numero = min(numeros)

    for valor in range(1,menor_numero+1):
        identifica_valor_mdc = list(map(lambda x: x % valor == 0, numeros))
        if False not in identifica_valor_mdc:
            maximo_divisor_comum = valor

    return maximo_divisor_comum






if __name__ =='__main__':
    # Primeira forma
    print(mcd_1([21,7]))
    print(mcd_1([125,40]))
    print(mcd_1([9,564,66,3]))
    print(mcd_1([55,22]))
    print(mcd_1([15,150]))
    print(mcd_1([7,9]))
    print(mcd_1([0,0,0]))

    print()
    # Segunda forma
    print(mcd_2([21,7]))
    print(mcd_2([125,40]))
    print(mcd_2([9,564,66,3]))
    print(mcd_2([55,22]))
    print(mcd_2([15,150]))
    print(mcd_2([7,9]))
    print(mcd_2([0,0,0]))

   
