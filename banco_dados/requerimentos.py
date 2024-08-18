try:
    from mysql import connector
    print('Modulo instalado.')
    
except ModuleNotFoundError:
    print('Modulo não instalado.')