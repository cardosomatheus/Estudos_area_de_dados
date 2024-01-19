import json
import os

caminho = os.path.join(os.getcwd(),r'python_udemy\POO\exercicio_json\arquivo_pessoa.json')
    
class Pessoa:
    def __init__(self, nome, sobrenome, idade): # inicializador da classe
        self.nome      = nome
        self.sobrenome = sobrenome
        self.idade     = idade 
        #self.caminho   =  os.path.join(os.getcwd(),r'python_udemy\POO\arquivo_pessoa.json')
    
    def salva_json(self, dicionario): # metodo da clase
        with open (caminho,'w') as pessoa_json:
            json.dump(dicionario, pessoa_json, ensure_ascii=False, indent=2)
        
        
    
    def cria_intancia(self, caminho_json): # metodo da clase
        with open(caminho_json, 'r') as ler_json: 
            ts= json.load(ler_json)
            self.__dict__ = ts 


p1 = Pessoa('Kaneki','Ken', 21)
p2 = Pessoa('vegeta','Ken', 50)
p3 = Pessoa('vegeta','Ken', 50)

pp = [p1.__dict__,p2.__dict__,p3.__dict__]

print(p1.salva_json(pp))


