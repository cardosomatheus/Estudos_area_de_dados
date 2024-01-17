class Camera:
    def __init__(self, nome, filmando=False):
        self.nome     = nome
        self.filmando = filmando
        
        
    def filmar(self):
        if self.filmando:
            print(self.nome,' Já está filmando')
            return
                
        self.filmando = True
        print(self.nome, ' está filmando...')
        
    def parar_filmar(self):
        if not self.filmando:
            print('Não está filmando')
            return
        
        self.filmando = False
        print(self.nome, 'Parando de filmar')


    def fotografar (self):
        if self.filmando:
            print(self.nome, 'Não é possivel fotografar pois está filmando...')
            return
        
        print(self.nome, 'fotografando') 
        
        
             
canon = Camera('canon')
sony  = Camera('Sony')
canon.filmar()
canon.filmar()
sony.filmar()
canon.parar_filmar()
canon.fotografar()
sony.filmar()
sony.filmar()
sony.fotografar()