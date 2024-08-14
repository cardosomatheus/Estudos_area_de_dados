compras = (
    {'Quantidade':2, 'preço':5,},
    {'Quantidade':3, 'preço':10},
    {'Quantidade':5, 'preço':15},
    {'Quantidade':8, 'preço':20}
)



if __name__ == '__main__':
    # (lambda valor_do_calcula: Quantidade x preço, dados usados no calcul)
    totais = tuple(
        map(
            lambda x: x['Quantidade'] * x['preço'], compras
        )
    )

    print(f'Total: {sum(totais)}')