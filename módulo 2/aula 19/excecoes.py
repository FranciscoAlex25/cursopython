a = 10 
b = 0 

# print(a / b)

try: 
    a / b 
except SystemError as e:
    print('erro: ', e)
    print('classe: ', e.__class__.__name__)
except ZeroDivisionError as e:
    print('erro: ', e)
    print('classe: ', e.__class__.__name__)
except Exception as e:
    print('erro: ', e)
    print('classe: ', e.__class__.__name__)


