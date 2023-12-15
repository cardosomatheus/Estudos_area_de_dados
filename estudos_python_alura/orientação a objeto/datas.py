class Data:

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        #   DATA FORMATADA DD/MM/YYYY
        print(self.dia,self.mes,self.ano, sep='/')
