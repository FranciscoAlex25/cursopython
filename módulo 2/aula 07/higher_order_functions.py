
def exibir(nome, idade):
    resposta = 'maior de idade' if idade >= 18 else 'menor de idade'
    return f'Olá {nome}, você é {resposta}'

def executar(function, *args):
    return function(*args)

resposta = executar(exibir, 'Alex', 22)

print(resposta)
