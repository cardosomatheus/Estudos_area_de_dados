class Humano:    
    def __init__(self, nome):
        self.nome = nome
        self._idade =  None

    especie = 'Homo Sapiens'


    def das_cavernas(self):
        self.especie = 'homo neanderthalensis'
        return self


    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,idade):
        if idade <0:
            raise ValueError('Idade menor que zero!!')
        self._idade = idade


    @staticmethod
    def especies():
        adjetivos = ('Habilid', 'Erectus','Neanderthalensis','Sapiens')
        return ('australopithecus',)+ tuple(f'Homo {adj}' for adj in adjetivos)


    @staticmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1] 


class Neanderthalensis(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]




if __name__=='__main__':
    badu = Humano('badu').das_cavernas()
    jose = Humano('jose')
    jose.idade = 50
    print(badu.especie)
    print(jose.especie)
    print(Humano.especies())
    print(Humano.is_evoluido(jose))
    print(Humano.is_evoluido(HomoSapiens))
    print(Humano.is_evoluido(Neanderthalensis))
    print(jose.idade)