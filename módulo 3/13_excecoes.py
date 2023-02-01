class MyError(Exception):
    ...


def show_error():
    print('Depois do erro!')
    raise MyError('Meu erro')

try:
    show_error()
except MyError as e:
    print(e.__class__.__name__)
