from datetime import datetime

class Pessoa:
    __ano_atual = int(datetime.now().year)
    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def get_ano_nascimento(self):
        return Pessoa.__ano_atual - self.idade
        
pessoa = Pessoa('Chaves', 80)  
print(pessoa.get_ano_nascimento())