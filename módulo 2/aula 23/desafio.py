# Exercício - Adiando execução de funções

def soma(x):
    def segundaFuncao(y):
        print(x + y)
    return segundaFuncao


def multiplica(x):
    def segundaFuncao(y):
        print(x * y)
    return segundaFuncao


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print()

soma_com_cinco(10)
multiplica_por_dez(10)
