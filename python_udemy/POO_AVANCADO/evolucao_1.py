class Humano:    
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    
    def das_cavernas(self):
        self.especie = 'homo neanderthalensis'
        return self


if __name__=='__main__':
    badu = Humano('badu').das_cavernas()
    jose = Humano('jose')


    print(badu.especie)
    print(jose.especie)