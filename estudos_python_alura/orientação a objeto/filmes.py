class filme:
    def __init__(self,nome,ano,duracao):
        self.__nome  = nome.title()
        self.ano     = ano
        self.duracao = duracao
        self.__like  = 0

    @property
    def like(self):
        return self.__like

    def dar_like(self):
        self.__like += 1
        
        
    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()



class serie:
    def __init__(self,nome,ano,duracao):
        self.__nome    = nome.title()
        self.ano       = ano
        self.temporada = duracao
        self.__like    = 0


    @property
    def like(self):
        return self.__like


    def dar_like(self):
        self.__like += 1


    @property 
    def nome(self):
        return self.__nome
    
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


    
        



vingadores = filme('vingadores - ultimato', 2018,160)
the_last   = serie('the last of US', 2023,1)


vingadores.dar_like()
the_last.dar_like()

print(f'nome: {vingadores.nome},ano: {vingadores.ano}, duracao: {vingadores.duracao}, likes: {vingadores.like}')
print(f'nome: {the_last.nome}, ano: {the_last.ano}, temporada: {the_last.temporada}, likes: {the_last.like}')


print(f'nome: {serie.nome}')
