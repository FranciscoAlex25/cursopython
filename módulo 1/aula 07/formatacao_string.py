# formatação de strigs # F strings

nome = 'Alex'
idade = 22
peso = 50
altura = 1.64
imc = peso / altura ** 2

print(f'meu nome é {nome} e tenho {idade} anos e possuo IMC de {imc:.2f}')
print('meu nome é {} e tenho {} anos e possuo IMC de {:.2f}'.format(nome, idade, imc))

'''
print('meu nome é {1} e tenho {0} anos e possuo IMC de {2:.2f}'.format(nome, idade, imc))
'''
print('meu nome é {nom} e tenho {ida} anos e possuo IMC de {im:.2f}'.format(nom=nome, ida=idade, im=imc))

