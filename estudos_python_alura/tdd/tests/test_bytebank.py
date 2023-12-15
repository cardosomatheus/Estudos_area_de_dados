import pytest
from pytest import mark
from codigo.bytebank import Funcionario


class Teste_Class:

    def test_quando_idade_13_03_2000_deve_retornar_23(self):
        #   GIVEN-CONTEXTO
        entrada = '13/03/2000'
        esperado = 23
        func_teste = Funcionario('teste', entrada, 1000)

        #   WHEN-ACAO
        resultado = func_teste.idade()

        #   THEN-DESFECHO
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_carvalho_deve_retornar_carvalho(self):
        #   GIVEN-CONTEXTO
        entrada = ' Lucas Carvalho'
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1000)

        #   WHEN-ACAO
        resultado = lucas.sobrenome()

        #   THEN-DESFECHO
        assert resultado == esperado




    def test_quando_decrescimo_salario_recebe_100_mil_deve_retornar_90_mil(self):
        #   GIVEN
        entrada = 100000
        entrada_nome = 'Paulo Braganca'
        esperado= 90000

        #   WHEN
        func_teste = Funcionario(entrada_nome, '11/11/2000', entrada)

        #   THEN
        resultado= func_teste.descrescimo_salario()

        assert resultado == esperado


    def test_quando_calcular_bonus_recebe_100_Deve_retornar_100(self):
        entrada = 1000
        esperado = 100
        func_teste = Funcionario('teste', '11/11/2000', 1000)

        resultado = func_teste.calcular_bonus()

        assert esperado == resultado


    def test_quando_calular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000

            func_teste = Funcionario('teste', '11/11/2000', 100000)
            resultado = func_teste.calcular_bonus()

            assert resultado

