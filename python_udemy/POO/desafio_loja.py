from datetime import datetime, timedelta
from loja import Cliente,Vendedor,Compra




if __name__ == '__main__':
    print('**'*10)
    vendedor_matheus = Vendedor(nome='Matheus',idade=23,salario=2000)
    vendedor_mara = Vendedor(nome='Mara',idade=27,salario=2000)


    cliente_1 = Cliente(nome='Jorge',idade=30)
    cliente_1.registra_compra(compra=Compra(vendedor=vendedor_matheus,data=datetime.now() - timedelta(days=15), valor=3000))
    cliente_1.registra_compra(compra=Compra(vendedor=vendedor_mara, data=datetime.now() - timedelta(days=10),valor=7000))


    print(cliente_1)
    print(cliente_1.get_data_ultima_compra())
    print(cliente_1.total_compras())