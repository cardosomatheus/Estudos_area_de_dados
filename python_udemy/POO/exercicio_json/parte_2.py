from parte1 import Pessoa, caminho
import json


with open(caminho, 'r') as ler_json: 
    dados= json.load(ler_json)
    #print(Pessoa(**dados[0]))
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])