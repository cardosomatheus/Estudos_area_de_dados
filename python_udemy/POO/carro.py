class Carro:
    def  __init__(self, nome = 'tt'):
        self.nome = nome
        
        
    def acelerar(self, velocidade):
        return f' {self.nome} está em  {velocidade + 10} km/h'



pp = Carro('fusca')
pq = Carro('camaro')

print(pp.acelerar(10))

print(pq.acelerar(100))


