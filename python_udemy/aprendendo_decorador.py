def fabrica_de_decoradores(a,b,c,):
    return fabrica_de_funcao

def fabrica_de_funcao(func):
    def interna(*args, **kwargs):
        print('decorando 1')
        for palavra in args:
             is_string(palavra)
        resultado = func(*args, **kwargs)
        print('decorado 2')
        return resultado
    return interna

@fabrica_de_funcao
def inverte_string(string):
    return string [::-1]


def is_string(param):
    if not isinstance(param,str):
        raise TypeError('parametro  deve ser setring')

#print(inverte_string('arroz'))



def decoradora(func):
    def interna(*args, **kwargs):
        for value in args:
            if not isinstance(value, (float, int)):
                raise TypeError('Apenas valores INT e FLOAT')
            
        resultado = func(*args, **kwargs)
        return resultado 
    return interna
 
@decoradora    
def soma(*args):
    print(soma.__name__)
    return sum(args)



print(soma(1,2,5,2))