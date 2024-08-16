from locale import LC_ALL,setlocale
from calendar import mdays, month_name
from functools import reduce

#print(month_name[1])
#print(mdays[1])

if __name__ == '__main__':
    setlocale(LC_ALL, 'pt_BR')
    meses_com_31_dias = [mes for index, mes in enumerate(month_name)  if mdays[index] == 31]
    print('Meses com 31 dias:', meses_com_31_dias)


    index_mes  = filter(lambda x : mdays[x] == 31, range(0,13))
    nome_meses = map(lambda x : month_name[x], index_mes)
    retorno = reduce(lambda todos,novo_mes : f'{todos} \n -{novo_mes}', nome_meses, 'meses com 31 dias:')
    print(retorno)
    
