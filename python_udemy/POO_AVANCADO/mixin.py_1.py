# Conceito de MixIn 

class MixToString:

    def __str__(self):
        html =  super().__str__().replace('(','<strong>(').replace(')',')<strong>')
        return f'<span>{html}<span>'

class Pessoa:
    def __init__(self, nome):
        self.nome = nome


    def __str__(self) -> str:
        return f'Sr. {self.nome}.'
    

class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet


    def __str__(self) -> str:
        return self.nome + ' (pet) ' if self.pet else ''


class HtmlPessoa(MixToString,Pessoa):
    pass


class HtmlAnimal(MixToString,Animal):
    pass

if __name__ == '__main__':
    pessoa1      = Pessoa('Matheus')
    pessoa_htlml = HtmlPessoa('Jose')
    animal       = Animal('Billy')
    animal_html  = HtmlAnimal('Ragnar')

    print(pessoa1)
    print(pessoa_htlml)
    print()
    print(animal)
    print(animal_html)