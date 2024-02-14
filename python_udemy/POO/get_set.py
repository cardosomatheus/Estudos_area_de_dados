class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
        
        
    @property
    def cor(self):
        print('GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('SETTER')
        self._cor = valor
    
    @property
    def cor_tampa(self):
        print('GETTER')
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, nova_cor_tampa):
        print('SETTER')
        self._cor_tampa = nova_cor_tampa


    
caneta = Caneta('Azul')
caneta.cor_tampa = 'Roxo'
caneta.cor = 'rosa'
print(caneta.cor_tampa)
#print (caneta.cor)
