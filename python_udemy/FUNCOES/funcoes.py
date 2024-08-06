import dados.dados_exercicios as exe

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


def liss_values():
    lista_completa = []
    while True:
        acao_lista = str(input('selecione uma opção: , [I] inserir [L] Listar [A] Apagar  [S] Sair: ')).upper()
        try:
            if acao_lista == 'I':
                valor = str(input('Informe o valor:'))
                exe.os.system('clear')
                lista_completa.append(valor)

            elif acao_lista == 'A':
                index_escolhido = int(input('Escolha um index para a ação: '))
                del (lista_completa[index_escolhido])

            elif acao_lista == 'L':
                exe.os.system('clear')
                if len(lista_completa) == 0:
                    print('A lista está vazia até o momento.')

                else:
                    for index, item in enumerate(lista_completa):
                        print(index, item)
            elif acao_lista == 'S':
                break

            else:
                print('opção incorreta.')
        except IndexError:
            print('Ação não realizada pois houve error com o index informado.')

        except ValueError:
            print('Index informado invalido, informe um numero inteiro.')


def generator_cpf():
    
    cpf_gerado = [str(exe.random.randint(0,9)) for i in range(0,9)]
    cpf_gerado = "".join(cpf_gerado)
    multiplicador_10 = 10
    multiplicador_11 = 11
    primeiro_digito_soma_valores = 0
    segundo_digito_soma_valores  = 0
    resto_divisao_primeiro_valor = 0
    resto_divisao_segundo_valor  = 0
    valida_cpf = len(cpf_gerado) < 9  or cpf_gerado == (cpf_gerado[0] * len(cpf_gerado)) 
    cpf_gerado = exe.re.sub(r'[^0-9]','', cpf_gerado)

    if valida_cpf is False:
        for i in cpf_gerado:
            i = int(i)
            primeiro_digito_valor = multiplicador_10 * i
            segundo_digito_valor  = multiplicador_11 * i
            primeiro_digito_soma_valores += primeiro_digito_valor
            segundo_digito_soma_valores  += segundo_digito_valor

            if multiplicador_10 == 2:
                # O resto da divisao entra os 9 valores se torna o 10º valor do cpf
                resto_divisao_primeiro_valor = (primeiro_digito_soma_valores * 10) % 11
                i = resto_divisao_primeiro_valor

            if multiplicador_11 == 2:
                resto_divisao_segundo_valor  = (segundo_digito_soma_valores * 10) % 11
                break 
            multiplicador_10 -= 1
            multiplicador_11 -= 1

        primeiro_digito = 0 if resto_divisao_primeiro_valor > 9 else  resto_divisao_primeiro_valor
        segundo_digito  = 0 if resto_divisao_segundo_valor > 9 else  resto_divisao_segundo_valor
        valores_finais  = str(primeiro_digito) + str(segundo_digito)
        cpf_final = cpf_gerado+'-'+valores_finais

        print('CPF:', cpf_final) 

    else:
        print('CPF  Invalido')


def deep_list_ascending():
    # Aumente os preços dos produtos a seguir em 10%
    # gere uma deep copy da lista
    # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
    
    produtos = exe.produtos_deep_copy
    deep_produtos= [{**i, 'preco': round(i['preco'] * 1.1,2)}  
                        for i in exe.copy.deepcopy(produtos)]
    produtos_ordenados_por_nome = sorted(deep_produtos, key= lambda  k: k['nome'])
    print('deep copy com preco + 10% ordenada:  ', *produtos_ordenados_por_nome, sep='\n')


def fatorial(n):
    if n <=1:
        return 1
    
    value = n * fatorial(n-1)
    print(value)
    return value
