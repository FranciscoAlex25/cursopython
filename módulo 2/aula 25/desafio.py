# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

lista1 = []


def zipper():
    cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    estados = ['BA', 'SP', 'MG', 'RJ']

    for i in range(len(cidades)):
        lista1.append((cidades[i], estados[i]))

    return lista1

print(zipper())

# def zipper(*cidades):
#     lista2 = [i for i in cidades]

#     def unir(*estados):
#         lista3 = [i for i in estados]

#         for i in range(len(lista2)):
#             lista1.append((lista2[i], lista3[i]))     

#         return(lista1)
    
#     return unir


# l1 = zipper(*['Salvador', 'Ubatuba', 'Belo Horizonte'])
# print(l1(*['BA', 'SP', 'MG', 'RJ']))
