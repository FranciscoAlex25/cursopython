'''
Criar variáveis para nome(str), idade(int), altura(float), e peso(float),
de uma pessoa. Criar variável com o ano atual (int). Obter o ano de nascimento
da pessoa (baseado na idade e ano atual). Obter o IMC da pessoa com duas casas
decimais (peso e na altura da pessoa). Exibir um texto com todos os valores na
tela usando F-String(com as chaves). 
'''

nome = 'Alex'
idade = 22
altura = 1.64
peso = 50
ano_nasc = 2022 - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'o IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')
