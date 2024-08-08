class Humano:    
    def __init__(self, nome):
        self.nome = nome
        self._idade =  None

    especie = 'Homo Sapiens'

    @property
    def inteligente(self):
        return NotImplementedError('error de classe abstrata.')

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


    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1] 


class Neanderthalensis(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False
class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True



if __name__=='__main__':
    badu = Humano('badu').das_cavernas()
    jose = Humano('jose')
    jose.idade = 50
    print(badu.especie,badu.idade)
    print(jose.especie, jose.idade)
    print(Humano.especies())
    print('Jose é inteligiente? ',jose.is_evoluido(),'///// Badu é inteligiente? ',badu.is_evoluido())
    print()

    # classes abstratas.
    try:
        anonimo = Humano('Anonimo')
    except NotImplementedError:
        print('Chora !!!!')


    jorge = HomoSapiens('Jorge')
    gronk = Neanderthalensis('gronk')
    print(f'{anonimo.nome} da classe {anonimo.__class__.__name__} é inteligente? {anonimo.inteligente}')
    print(f'{jorge.nome} da classe {jorge.__class__.__name__} é inteligente?  {jorge.inteligente}')
    print(f'{gronk.nome} da classe {gronk.__class__.__name__} é inteligente?  {gronk.inteligente}')

