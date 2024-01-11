import emoji


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

