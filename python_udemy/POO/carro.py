class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        

    def falar_nome_classe(self):
        print(f'nome {self.nome} {self.sobrenome} classe: {self.__class__.__name__}')

class Cliente(Pessoa):
    ...
    


class Aluno(Pessoa):
    ...
    
    
    
c1 = Cliente('luiz', '2')
a1 = Aluno('joao', '3')

c1.falar_nome_classe()
print()
a1.falar_nome_classe()