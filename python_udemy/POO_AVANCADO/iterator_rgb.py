class RGB:
    def __init__(self):
        self.rgb = ['red','green','blue'][::-1]


    def __iter__(self):
        return self    
    
    
    def __next__(self):
        try:
            return self.rgb.pop()
        except IndexError as e:
            raise StopIteration()
        


if __name__ ==  '__main__':
    # Usando __next__ para pegar o proximo elemetno.
    cor_rgb = RGB()
    print(cor_rgb.__next__())
    print(cor_rgb.__next__())
    print(cor_rgb.__next__())
        
    # Usando o metodo __iter__ para fazer loop direto no objeto.
    for cor in RGB():
        print(cor)
