#   MODULOS
from conta import Conta
from cliente import Cliente
from datas import Data


#   DATA FORMADATA
D = Data(10,8,2007)
D.formatada()
print('*'*10)
#   Cliente como modigicar um cliente
cliente = Cliente('mathe')  #   Definindo um cliente
print(cliente.nome)         #   Mostrando o cliente
cliente.nome = 'joao'       #   Alterando o cliente

print('*'*10)
#   CONTAS CRIADAS
conta  = Conta(123,"matheus",50,1000.0)
conta2 = Conta(321,"marcos",100,1000.0)

print(conta2.limite)            #   Limite atual da conta
conta.limite = 1500             #   Alterando o limite da conta para 1500
conta.sacar(80)                #   Tentando sacar o valor da conta  
print(conta.saldo)              #   Saldo atual da conta
print(conta.cod_banco)          #   Codigo do banco
print(conta.codigos_banco())    #   Codigo dos bancos
print('*'*10)
