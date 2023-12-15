# BIBLIOTECA E MODULOS
from random import randint

def jogar():
    print('*'*10)
    print('TESTE DE ADIVINHAÇÃO')
    print('*'*10)

    pontos = 1000
    numero = randint(1,100)

    print('escolha o nivel de dificuldade')
    print('(1)- facil, (2) medio,  (3) dificil')
    nivel = int(input('Defina o nivel: '))

    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 5
    elif nivel == 3:
        tentativas = 3

    for rodadas in range(tentativas):
        chute_numero = int(input('chute um numero entre 1 e 100: '))
        if chute_numero == numero:
            print(f'acertou, fim do jogo, numero informado {numero}')
            break
        elif chute_numero < numero:
            print(f'o chute foi um valor menor que o numero. chute: {chute_numero}.')
        elif chute_numero > numero:
            print(f'o chute foi um valor maior que o numero. chute : {chute_numero}')

        pontos_perdidos = abs(numero - chute_numero) # o retorno é um valor positivo sempre
        pontos = pontos - pontos_perdidos 

    print('fim do jogo!')
    print(f'pontuação final: {pontos}')

if __name__ == "__main__":
    jogar()