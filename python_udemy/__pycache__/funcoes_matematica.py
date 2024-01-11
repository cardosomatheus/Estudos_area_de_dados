def multiplica_valor(*args):
    total = 1
    for i in args:
        print(i)
        total *= i
    
    return total


def number_par_impar(pvalor):
    try:
        if isinstance(pvalor, int):
            return 'par' if pvalor % 2 == 0 else 'impar'
        
        else:
            raise ValueError()
    except ValueError:
        print('O valor não é um numero inteiro!!')




def multiplicado_por(valor_multiplador):
    def numero_multiplicado(numero):
        return numero * valor_multiplador
    
    return numero_multiplicado


def perguntas_matematicas():
    perguntas = [
        {
            "pergunta": 'Qaunto é 2+2',
            "opcoes":['1','2','3','4'],
            "resposta":'4'
        },
        {
            "pergunta": 'Qaunto é 3+3',
            "opcoes":['7','6','8','4'],
            "resposta":'6'
        },
        {
            "pergunta": 'Qaunto é 25/5',
            "opcoes":['7','6','4','5'],
            "resposta":'5'
        }
    ]

    perguntas_acertadas = 0
    total_perguntas = 0
    for pergunta in perguntas:
        total_perguntas +=1 
        print('Pegunta:', pergunta["pergunta"], '?' )
        opcoes_index = {}

        for index, opcao in enumerate(pergunta["opcoes"]):
            print(index,')', opcao)
            opcoes_index[str(index)] = opcao

        while True:
            resposta_escolhida = str(input('Escolha uma opção:'))
            if resposta_escolhida in opcoes_index.keys():
                if opcoes_index[resposta_escolhida] == pergunta["resposta"] :
                    mensagem = emoji.emojize('Acertou :thumbs_up: ,  a opção correta é')
                    perguntas_acertadas +=1
                else:
                    mensagem = emoji.emojize('Errou :thumbs_down:,  a opção correta é')

                print(mensagem)
                break
            else:
                print('Opção invalida!!')

    print(f'Voce acertou {perguntas_acertadas} de {total_perguntas}')



duplicar  = multiplicado_por(2)
triplicar    = multiplicado_por(3)
quaduplicar  = multiplicado_por(4)




#print(duplicar(5), triplicar(5), quaduplicar(5))
#print(multiplica_valor(1,2,3,4,5,6,7))
#print(number_par_impar(10))
#perguntas_matematicas()