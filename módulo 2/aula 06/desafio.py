# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

multiplicador = 1

def multiplicar(*args):
    global multiplicador

    for i in args:
        multiplicador *= i
    
    return multiplicador

resultado = multiplicar(1, 3, 6, 3, 3)
print(resultado)
