# Assim que o Try encontra um erro ele pula para o Except

try:
    a = int('a')
    print(a)
except:
    print('Erro de valor!')
