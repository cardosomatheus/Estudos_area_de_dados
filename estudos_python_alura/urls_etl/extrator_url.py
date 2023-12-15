#BIBLIOTECAS
import re 

#CLASSES
class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def __str__(self):
        #   Retorna a url passada e o seus parametros separados
        return f'URL:{self.url}\n Parametros:{self.get_url_parametros()}\n URL BASE:{self.get_url_base()}'
    
    def __len__(self):
        #   Retorna o tamanho da url
        return len(self.url)
    
    def __eq__(self,other):
        #   Define se o valor e null ou ''
        return self.url == other.url
    
    def sanitiza_url(self,url):
        #   Tratamento de url com espaços
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        # Valida se a url passada está de acordo com as condições
        if not self.url:
            raise ValueError("A URL ESTÁ VAZIA!")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        
        if not match:
            raise ValueError("URL invalida")

    def get_url_base(self):
        #   busca a url base até o primeiro ponto de interrogação (?).
        indice_interrogacao = self.url.find('?')
        url_base            = self.url[:indice_interrogacao]    
        return url_base

    def get_url_parametros(self):
        #   busca os parametros da url apartir do primeiro ponto de interrogação (?).
        indice_interrogacao = self.url.find('?')
        url_parametros      = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self,parametro_busca):
        # O usuario passa o parametro desejado e se ele existir dentro da url é retornado.
        indice_parametro   = self.get_url_parametros().find(parametro_busca)
        indice_valor       = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def get_quantidade(self):
       #    retorna a quantidade na url em formato integer
       return int(self.get_valor_parametro('quantidade'))


    def cotacao(self):
        # Cotação de cada moeda(Dolar,Real) após o calculo de quantidade e conversão de moeda
        cotacao_dolar = 5.50
        cotacao_real  = 1.0 
        moeda_origem  = self.get_valor_parametro('moedaOrigem')
        moeda_destino = self.get_valor_parametro('moedaDestino')

        if moeda_origem == 'real' and moeda_destino == 'dolar':
            return (self.get_quantidade() * cotacao_real) * cotacao_dolar
        
        elif moeda_origem == 'dolar' and moeda_destino == 'real':
            return (self.get_quantidade() * cotacao_dolar) / cotacao_real
        
        elif moeda_origem == 'real' and moeda_destino == 'real':
            return self.get_quantidade() * cotacao_dolar
        
        elif moeda_origem == 'dolar' and moeda_destino == 'dolar':
            return self.get_quantidade() * cotacao_dolar
        else:
            raise ValueError(f'conerção de {moeda_origem} para {moeda_destino} invalida')



#resultados 
url = 'bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
extrator_url = ExtratorURL(url)
print(f'URL BASE: {extrator_url.get_url_base()}')
print(f'Parametros da URL: {extrator_url.get_url_parametros()}')
print(f'Quantidade para conversão{extrator_url.get_quantidade()}')
print(f'Cotação final: {extrator_url.cotacao()}')
