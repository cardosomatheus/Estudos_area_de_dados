class Funcionario:
    def __init__ (self,nome):
        self.nome = nome
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class hipster:
    def __str__(self):
        return f'hipster: {self.nome}'      

class junior(Alura):
    pass

class pleno(Alura,Caelum):
    pass

class senior(Alura,Caelum,hipster):
    pass


matheus = junior('matheus')
jose    = pleno('jose')
perillo = senior('perillo')

matheus.busca_perguntas_sem_resposta()
jose.busca_perguntas_sem_resposta()
perillo.mostrar_tarefas