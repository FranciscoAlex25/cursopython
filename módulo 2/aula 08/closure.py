lista = []

def receberValor(vezes):
    def apresentar(rep):
        lista.clear()
        for i in range(vezes):
            lista.append(rep)
        return lista
    return apresentar

valor1 = receberValor(10)
valor2 = receberValor(7)

print(valor1(3))
print(valor2(4))
