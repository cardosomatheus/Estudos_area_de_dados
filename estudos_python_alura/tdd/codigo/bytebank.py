from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    def sobrenome(self):
        nome_completo = self.nome.split(' ')
        return nome_completo[-1]

    def _diretor(self):
        sobrenome_chefs = ['Braganca', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Ptolomeu']
        return self._salario >= 100000 and (self.sobrenome() in sobrenome_chefs)

    def descrescimo_salario(self):
        if self._diretor():
            self._salario = self._salario - (self._salario * 0.1)
        return self._salario

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]

        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salario é muito alta para receber um bônus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
