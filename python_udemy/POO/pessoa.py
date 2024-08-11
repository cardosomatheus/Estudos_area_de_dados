from datetime import datetime

class Pessoa:
    __ano_atual = int(datetime.now().year) # Atributos de classe
    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def get_ano_nascimento(self):   # metodo normal de classe
        return Pessoa.__ano_atual - self.idade
    
    
    @classmethod # Voce pode chamar o mmetodo sem  o parametro de entrada self
    def metodo_de_classe(cls):
        print('hey')        
    


pessoa = Pessoa('Chaves', 80)  
print(pessoa.get_ano_nascimento)
pessoa.metodo_de_classe()

