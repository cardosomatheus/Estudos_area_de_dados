# BIBLIOTECA E MODULOS
from random import randrange


def mensagem_abertura():
    print('*'*10)
    print('**BEM VINDO AO JOGO DA FORCA**')
    print('*'*10)


def leitura_arquivotxt ():
    with open('frutas.txt', 'r') as arq:
        frutas = []
        for fruta in arq:
            frutas.append(fruta.strip())
    numero_da_fruta = randrange(0,len(frutas))
    palavra_secreta = frutas[numero_da_fruta].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return  ["_" for letra in palavra]


def mensagem_vencedora():
    print('*'*30)
    print('**parabens, voce ganhou!*****')
    print('*'*30)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    

def mensagem_perdedora():
    print('*'*30)
    print('**infelizmente, voce perdeu!**')
    print('*'*30)
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
      
    mensagem_abertura()
    palavra_secreta = leitura_arquivotxt()
    letras_acertadas =inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute_letra = str(input('CHUTE UMA LETRA:')).strip().upper()
        
        if chute_letra in palavra_secreta:
            #se o chute conter uma letra em palavra secreta:
            index = 0 
            for letra in palavra_secreta:
                # loop por letra em palavra secreta
                if chute_letra == letra:
                    # se o chute for igual a uma letra da palavra secreta
                    # adicionamos ela na lista de letra_acertadas atraves do index 
                    letras_acertadas[index] = letra
                index += 1
        else:
            # se o chute não conter uma letra em palavra secreta, adicionamos um erro
            erros += 1
            desenha_forca(erros)

         # Condições de parada
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        
    if acertou:
        mensagem_vencedora()

    else:
        mensagem_perdedora()        
    


if __name__ == "__main__":
    jogar()