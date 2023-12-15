#   Biblioteca
from validate_docbr import CPF,CNPJ


#   Classes
class Documento:
    @staticmethod
    def cria_documento(documento):
        """metodo pai que verifica se o valor passado é um CPF ou CNPJ 
            e passa o valor para a classe filha especialida """
        if len(documento) == 11:
            return Doc_cpf(documento)
        
        elif len(documento) == 14:
            return Doc_cnpj(documento)
        
        else:
            raise ValueError("DOCUMENTO INVALIDO")
        
class Doc_cpf:
    def __init__(self,documento):
        """ Clase filha que valida se CPF é valido e se for:
            self.cpf recebe o valor de documento"""
        if self.validar(documento):
              self.cpf = documento

        else:
            raise ValueError('CPF INVALIDO !!!')    

    def __str__(self):
        """retorna p cpf com mascara"""
        return self.formatar()
    

    def validar(self,documento):
        """valida o CPF"""
        validador = CPF()
        return validador.validate(documento)

    def formatar(self):
        """retorna CPF formatado"""
        mascara = CPF()
        return mascara.mask(self.cpf)

class Doc_cnpj:

    def __init__(self,documento):
        """ Clase filha que valida se CNPJ é valido e se for:
            self.cpf recebe o valor de documento"""
        if len(documento) == 14:
         self.cnpj = documento
    
        else:
            raise ValueError('CNPJ INVALIDO !!!')  
    
    def __str__(self):
        """retorna p cnpj com mascara"""
        return self.formatar()


    def validar(self,documento):
        """valida o CNPJ"""
        validador_cnpj= CNPJ()
        return validador_cnpj.validate(documento)
        

    def formatar(self):
        """retorna p cnpj com mascara"""
        mascara = CNPJ()
        return mascara.mask(self.cnpj)    
