from datetime import datetime

class Compra():
    def __init__(self, vendedor, data=datetime.now(), valor=0):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor