nomes  = (
    {'NOME': 'Matheus',  'IDADE' : 23},
    {'NOME': 'Jose', 'IDADE' : 35},
    {'NOME': 'Sergio','IDADE' : 70},
    {'NOME': 'Claudio','IDADE' : 50}
)
    
    
if __name__ == '__main__':
    nomes_com_mais_de_4_letras = list(filter(lambda x: len(x['NOME']) > 4,nomes))
    print(nomes_com_mais_de_4_letras)