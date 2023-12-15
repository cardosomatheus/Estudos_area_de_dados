#   Biblioteca
import re


#   Classes
class Telefones:
    def __init__(self, telefone):
        """valida se o telefone é valida e se for:
            self.numero recebe o valor informado"""
        if self.valida_telefone(telefone):
            self.numero = telefone
        
        else:
            raise ValueError("numero de telefone incorreto !!!!!")

    def valida_telefone(self, telefone):
        """retorna se o telefone é valido """
        padrao = "[0-9]{2,3}?[0-9]{2}[0-9]{5}[0-9]{4}"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False
        
    def formatar_telefone(self):
        """formata o numero em formato de telefone """
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.numero)
        return f'+{resposta .group(1)} ({resposta .group(2)}) {resposta .group(3)}-{resposta .group(4)}'
    