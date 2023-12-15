# BIBLIOTECA E MODULOS
import forca
import advinhacao


def escolher_jogo():
    print('*'*15)
    print('ESCOLHA O SEU JOGO')
    print('(1) forca, (2) advinhaçao')
    print('*'*15)

    escolha_jogo = int(input('ESOLHA A OPÇÃO DO JOGO:'))

    if escolha_jogo == 1:
        print('jogando forca')
        forca.jogar()
    elif escolha_jogo == 2:
        print('jogando advinhação')
        advinhacao.jogar()
    

escolher_jogo()