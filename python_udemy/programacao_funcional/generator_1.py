def cores_arco_iris():
    yield 'vermelho' 
    yield 'laranja' 
    yield 'amarelo' 
    yield 'verde'
    yield 'azul'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'


def sequence():
    num = 0
    while True:
        num  += 1
        yield num

    


if __name__ == '__main__':
    seq = sequence()
    for cor in cores_arco_iris():
        print(cor)

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    
    