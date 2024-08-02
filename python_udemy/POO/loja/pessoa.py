class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    

    def __str__(self):
        return f'Sr(a) {self.nome} com {self.idade} anos.'
    

    def e_adulto(self):
        return 'Adulto'  if self.idade >= 18 else 'Jovem'
