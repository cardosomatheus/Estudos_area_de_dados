class Humano:    
    def __init__(self, nome):
        self.nome = nome

    especie = 'Homo Sapiens'


    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


    @staticmethod
    def especies():
        adjetivos = ('Habilid', 'Erectus','Neanderthalensis','Sapiens')
        return ('australopithecus',)+ tuple(f'Homo {adj}' for adj in adjetivos)


    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1] 


class Neanderthalensis(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]




if __name__=='__main__':
    badu = Humano('badu').das_cavernas()
    jose = Humano('jose')

    print(Humano.is_evoluido())
    print(HomoSapiens.is_evoluido())
    print(Neanderthalensis.is_evoluido())
    print(badu.especie)
    print(jose.especie)
    print(jose.especies())
    print(HomoSapiens.is_evoluido())
    print(jose.is_evoluido())
    print(badu.is_evoluido())
