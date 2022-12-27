'''
remove(value) - append() - pop(indice) - clear() - del() - insert() -
'''

nomes = ['alex', 'karol', 'julio', 'matheus']
senha = (12345)

a, *_ = nomes

for i in range(len(nomes)):
    print(f'{i} - {nomes[i]}')

print(a)
print(_)
