#   Bibliotecas
from datetime import datetime,timedelta

#   Classes
class Datasbr:

    def __init__(self):
        """retorna a data e hora do momento do cadastros"""
        self.momento_cadastro = datetime.today()
    
    def __str__(self):
        """retorna a data formatada em formato brasileiro"""
        return self.data_formatada()

    def mes_cadastro(self):
        """retorna o mes por extenso do cadastro"""
        meses_ano = ["janeiro","fevereiro","março","abril","maio","junho","julho",
                     "agosto","setembro","outubro","novembro","dezembro"]
        
        mes_cadastro = self.momento_cadastro.month -1
        return meses_ano[mes_cadastro]

    def dia_semana(self):
        """retorna o dia da semana por extenso do cadastro"""
        dia_semana=["segunda-feira","terça-feira","quarta-feira","quinta-feira",
                    "sexta-feira","sabado-feira","domingo-feira"]
        
        semana_cadastro = self.momento_cadastro.weekday()
        return dia_semana[semana_cadastro]
    
    def data_formatada(self):
        """retorna a data formatada em formato BR"""
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M:%S")

    def tempo_cadastro(self):
        """ retorna a diferencao do dia do cadastro com o dia atual"""
        tempo_cadastro = (datetime.today()+ timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
    