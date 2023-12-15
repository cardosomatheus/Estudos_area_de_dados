#libs
import csv, pickle, json
from contato import Contato


def csv_para_contatos(caminho,encode):
    # retorna a lista dos dados em lista
    contatos = []

    try:
        with open(caminho, encoding=encode, mode='r') as arquivo:
            for linha in csv.reader(arquivo):
                vid    = linha[0]
                vnome  = linha[1]
                vemail = linha[2]

                vcontato = Contato(vid, vnome, vemail)
                contatos.append(vcontato) 

    except FileNotFoundError:
        print('arquivo não encontrado!!')

    except PermissionError:
        print('Permissão negada para a ação desejada!!')

    return contatos


def contatos_para_pickle(contatos,caminho):
    # Escrita de arquivo pickle (binario)
    with open(caminho, mode='wb') as arquivo:    
        pickle.dump(contatos,arquivo)


def pickle_para_contatos(caminho):
    # Leitura de arquivo pickle (binario)
    with open(caminho, mode='rb') as arquivo:    
        contatos =  pickle.load(arquivo)
    
    return contatos
    

def contatos_para_json(contatos,caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos,arquivo, default= lambda contato: contato.__dict__)


def json_para_contato(caminho):
    lista_contatos = []

    with open(caminho, mode='r') as arquivo:
        for contato in json.load(arquivo):
            cs = Contato(**contato)
            lista_contatos.append(cs)

    return lista_contatos