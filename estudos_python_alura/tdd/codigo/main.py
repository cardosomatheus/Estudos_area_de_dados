from codigo.bytebank import Funcionario
import pytest 

p = pytest

ana = Funcionario('ANA PAULA', '13/03/2000', 100000)
#lucas = Funcionario('Lucar Carvalho','13/03/2000',1000)
#print(lucas.idade())
print(ana.calcular_bonus())