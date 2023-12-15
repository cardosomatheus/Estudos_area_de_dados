#   Bibliotecas
import requests

#   Classes
class Busca_Cep:
    def __init__(self,cep):
        """
        Através da função: valida_cep() valida se o cep e valido e se for for: 
        self.cep = recebe o cep informado
        """
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP INVALIDO")
            

    def  __str__(self) -> str:
        """retorna o CEP com mascara"""
        return self.formata_cep()
    
    
    def valida_cep(self,cep):
        """Valdia o veracidade do CEP"""
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formata_cep(self):
        """ formata o cep em formato brasileiro"""
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    def acessa_viacep(self):
        """Através de uma API, busca o bairro,endereco e logradouro do CEP"""
        url = f"https://viacep.com.br/ws/{self.cep}/json"
        r = requests.get(url)
        json = r.json()
        return (json['bairro'],
                json['localidade'],
                json['logradouro'])
    