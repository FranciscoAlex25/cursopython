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


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
lista1 = []


def zipper(*args1):
    lista2 = [i for i in args1]

    def unir(*args2):
        lista3 = [i for i in args2]

        for i in range(len(lista2)):
            lista1.append((lista2[i], lista3[i]))         
        print(lista1)

    return unir


l1 = zipper(*cidades)
l1(*estados)
