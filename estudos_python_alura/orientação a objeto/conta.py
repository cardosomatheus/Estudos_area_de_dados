class Conta:
    
    def __init__(self,numero,titular,saldo,limite):
        print(f'construindo objeto.....{self}')
        self.__numero    = numero
        self.__titular   = titular
        self.__saldo     = saldo
        self.__limite    = limite
        self.__cod_banco = '001'


    def extrato(self):
        #   Extrato da conta do cliente
        print(f'saldo: {self.__saldo}, titular: {self.__titular}')


    def depositar(self,valor):
        #   Desposita um valor desejado na conta 
        self.__saldo += valor
        print(f'novo saldo com o deposito: {self.__saldo}Titular: {self.__titular}')


    def __pode_sacar(self,saque_desejado):
        saque_dispoivel = self.__saldo + self.__limite
        #   Retorno booleano se é possivel sacar o valor desejado
        return saque_desejado <= saque_dispoivel


    def sacar(self,saque_desejado):
        if self.__pode_sacar(saque_desejado):   
            #retorna True se o valor for possivel sacar
            self.__saldo -= saque_desejado
            print(f'novo saldo com a retirada: {self.__saldo}.Titular: {self.__titular}')

        else:
            #   Se o retorno for False, o saque não é efetuado
            print('o valor supera o estimado')
    

    def tranferir(self,valor,conta_destino):
        # saca um valor da conta do cliente e tranfere para a conta_destino
        self.sacar(valor)
        conta_destino.depositar(valor)
        print('tranferencia conlcuida')


    @property
    def saldo(self):
        # Retorna o saldo atual da conta do usuario
        return self.__saldo


    @property
    def titular(self):
        # Retorna o titular da conta do usuario
        return self.__titular


    @property
    def numero(self):
        # Retorna o numero da conta do usuario
        return self.__numero


    @property
    def limite(self):
        print('limite da conta')
        # Retorna o limite da conta do usuario
        return self.__limite


    @limite.setter 
    def limite(self,novo_limite):
        #   Alteração do limite do usuario.
        print('limite alterado com sucesso')
        self.__limite = novo_limite


    @staticmethod
    def cod_banco():
        # Codigo do banco aatual, ou seja BB
        return "001"


    @staticmethod
    def codigos_banco():
        #   Retorna uma lista com bancos e seus codigos
        return {'BB': '001','Caixa': '104','Bradesco':'237'}
