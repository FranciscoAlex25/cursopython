
def apresentacao(nome, idade):
    resposta = 'é maior de idade' if idade >= 18 else 'é menor de idade'
    print(f'Olá {nome}, você {resposta}')


apresentacao(nome='alex', idade=22)
apresentacao(nome='pedro', idade=12)
