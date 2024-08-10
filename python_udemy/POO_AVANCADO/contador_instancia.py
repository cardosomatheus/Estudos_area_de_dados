class  ClasseSimples:
    contador = 0
    
    def __init__(self) -> None:
        ClasseSimples.contador +=1 
        #self.contar_classe()
            
    #@classmethod
    #def contar_classe(cls):
    #    cls.contador += 1




if __name__ == '__main__':
    lista = [ClasseSimples(),ClasseSimples(),ClasseSimples(),ClasseSimples()]
    print(ClasseSimples.contador)