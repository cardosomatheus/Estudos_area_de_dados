def zipper(lista_1, lista_2):
    tamanho_menos_lista = min(len(lista_1),len(lista_2))
    return [(lista_1[i], lista_2[i]) for i in range(tamanho_menos_lista)]


# ambos retornam o mesmo.
print(zipper(['1','2'],['2','1','2','3']))
print(list(zip(['1','2'],['2','1','2','3'])))