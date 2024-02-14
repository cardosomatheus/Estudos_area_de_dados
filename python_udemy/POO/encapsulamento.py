"""
public = pode ser acessada de qualquer lugar
proteced = Só é acessado na sua classe e suas sub classes
private = Só pode ser usado em sua classe 

"""
class Foo:
    def __init__(self) -> None:
        self.public = 'publico'
        self._protected = 'acesso na sua classe e suas sub classes'
        self.__private  = 'Acesso apenas em sua classe'