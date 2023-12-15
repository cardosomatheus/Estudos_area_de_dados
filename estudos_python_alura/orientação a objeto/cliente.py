class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        #   Busco o nome do cliente
        print('Chamando a @property')
        return self.__nome.title()

    @nome.setter 
    def nome(self,novo_nome):
        print('alterando o nome do cliente')
        self.__nome = novo_nome
