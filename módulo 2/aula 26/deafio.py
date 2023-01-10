"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4]
lista_c = []


def verificarMaior(func):
    def verificar(lista1, lista2):
        if len(lista1) >= len(lista2):
            return func(lista2, lista1)
        return func(lista1, lista2)
    return verificar 


@ verificarMaior
def somarLista(lista1, lista2):
    for i in range(len(lista1)):
        lista_c.append(lista1[i] + lista2[i])
    return lista_c


print(somarLista(lista1, lista2))
