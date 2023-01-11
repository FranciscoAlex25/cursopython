fatorial = 1
valores = []


def fatorar(fator=5):
    global fatorial

    valores.append(fator)
    fatorial *= fator
    fator -= 1

    if fator < 1:
        return [fatorial, valores]

    return fatorar(fator)


fatoral_e_lista =  fatorar(2)

for i in fatoral_e_lista[1]:
    if i == 1:
        print(i, '=', fatoral_e_lista[0])
        break
    print(f'{i} x', end=' ')
