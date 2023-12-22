
def imc_body(peso, altura_metros):
    caluclo_imc = round(peso / (altura_metros * altura_metros), 2)
    print('IMC:', caluclo_imc)


def bigger_value(valor_1, valor_2):
    if valor_1 > valor_2:
        print('maior valor:', valor_1)
    elif valor_1 == valor_2:
        print('valores iguais:', valor_1, ' =', valor_2)
    elif valor_1 < valor_2:
        print('maior valor:', valor_2)
    else:
        print('nda')


def name_age(nome, idade):
    vespacos = 'não contem espacos'

    if ' ' in nome:
        vespacos = 'contem espacos'

    if nome and idade is not None:
        print('Nome:', nome)
        print('Nome invertido:', nome[::-1])
        print('O seus nome', vespacos)
        print('Primeira letra:', nome[0])
        print('Ultima letra:', nome[-1])
    else:
        print('Campos Vazios')


def number_par_inpar(pvalor):
    try:
        if isinstance(pvalor, int):
            numero_par = 'Valor Impar'

            if pvalor % 2 == 0:
                numero_par = 'Valor Par'
        else:
            raise ValueError()

        print('valor:', pvalor, 'É um valor', numero_par)

    except ValueError:
        print('O valor não é um numero inteiro!!')


def current_time(current_time):
    try:
        if isinstance(current_time, int):
            if current_time >= 0 and current_time <= 11:
                print('Bom dia 0-11', 'hora atual:', current_time)

            elif current_time >= 12 and current_time <= 17:
                print('Boa tarde 12-17', 'hora atual:', current_time)

            elif current_time >= 18 and current_time <= 23:
                print('Boa noite 18-23', 'hora atual:', current_time)
            else:
                print('horario informado indefinido, informe uma hora entre 0 e 23.')
        else:
            raise ValueError()

    except ValueError:
        print('O valor não é um numero inteiro!!')


def size_first_name(pfirst_name):
    primeiro_nome = str(pfirst_name)
    size_name = len(primeiro_nome)

    if size_name >= 1 and size_name <= 4:
        print('Seu nome é curto.')

    elif size_name >= 5 and size_name <= 6:
        print('Seu nome é normal.')

    elif size_name > 6:
        print('Seu nome é muito grande.')

    else:
        print('Digite mais que uma Letra.')


def using_while(nome):
    contador = 0
    novo_nome = ''

    while contador < len(nome):
        print(nome[contador])
        novo_nome += '*'+nome[contador]
        contador += 1
    print(novo_nome)


def basic_calculator(first_value, second_value, operador):
    while True:
        sair = str(input('Quer sair [S/N]: ')).lower().startswith('s')
        numeros_valido = None
        if sair:
            break

        operador_permitidos = '*/+-'
        try:
            primeiro_valor = float(first_value)
            segundo_valor = float(second_value)
            operdor_matematico = str(input('Operador (+-/*): '))
            numeros_valido = True

            if numeros_valido is None:
                print('Um dos numero digitados são invalidos.')
                continue

            if operdor_matematico not in operador_permitidos:
                primeiro_valor('Operador invalido, os permitidos são (+-/*)')
                continue

            elif len(operdor_matematico.strip()) > 1:
                primeiro_valor('digite apenas um operador.')
                continue

            print('relaizando a conta')

            if operdor_matematico == '+':
                conta_realizada = primeiro_valor + segundo_valor

            elif operdor_matematico == '*':
                conta_realizada = primeiro_valor * segundo_valor

            elif operdor_matematico == '/':
                conta_realizada = primeiro_valor / segundo_valor

            elif operdor_matematico == '-':
                conta_realizada = primeiro_valor - segundo_valor

            print('Valor do calculo:', conta_realizada)

        except ValueError:
            print('Valor indefinido.')

        except ZeroDivisionError:
            print('O segundo valor (dividento) não pode ser 0 na divisão')
