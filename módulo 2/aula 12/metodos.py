import copy 

dicionario = {
    'nome': 'alex',
    'idade': 22, 
    'lista': [1, 2, 3, 4]
}

dict1 = copy.deepcopy(dicionario)

print(id(dicionario))
print(id(dict1))
