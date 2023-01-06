
def dividir(n1, n2): 
    try: 
        a = n1 / n2
        return a
    except:
        raise ZeroDivisionError('Divisão por zero')


dividir(2, 0)
