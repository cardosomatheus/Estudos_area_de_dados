from .pessoa import Pessoa
from .compra import Compra


class Cliente(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome=nome,idade=idade)
        self.compras = []
    

    def __str__(self):
        return ''.join([f'vendedor: {item.vendedor} da compra: {item.valor}.\n' for item in self.compras])


    def registra_compra(self,compra):
        self.compras.append(compra) if isinstance(compra,Compra) else 'Não é uma Compra!!'


    def get_data_ultima_compra(self):
        return f'Maior data: {max([item.data for item in self.compras])}'


    def total_compras(self):
        return f'Total: {sum([ item.valor for item in self.compras])}'