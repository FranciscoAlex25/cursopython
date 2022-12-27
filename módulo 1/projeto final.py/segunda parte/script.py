cpf = '462.945.480-20'
soma = contador = valor = primeiro_digito = 0 

# listas necessárias
lista_com_valores_regressiva = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista_com_valores_multiplicados = []

# obetendos os dígitos separadamente
lista_com_9_digitos = cpf.split('.') 
lista_com_3_primeiros_digitos = list(lista_com_9_digitos[0])
lista_com_3_segundos_digitos = list(lista_com_9_digitos[1])
lista_com_3_ultimos = list(lista_com_9_digitos[2].split('-')[0])
lista_oficial = lista_com_3_primeiros_digitos + lista_com_3_segundos_digitos + lista_com_3_ultimos

# dicionando os valores multiplicados à lista
for i in range(2, 11):
    valor = int(lista_com_valores_regressiva[contador]) * int(lista_oficial[contador])
    lista_com_valores_multiplicados.append(valor)
    contador += 1

# somando os valores da lista
for i in lista_com_valores_multiplicados:
    soma += int(i)

# operações necessárias
resultado = (soma * 10) % 11

# obtendo o dígito 
primeiro_digito = resultado if resultado <= 9 else 0

# ----------------------------------------------------------------------------------------
soma = 0 
resultado = 0 
contador = 0

# listas necessárias
lista_com_valores_regressiva = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
lista_com_valores_multiplicados = []
lista_oficial.append(primeiro_digito)

# dicionando os valores multiplicados à lista
for i in range(2, 12):
    valor = int(lista_com_valores_regressiva[contador]) * int(lista_oficial[contador])
    lista_com_valores_multiplicados.append(valor)
    contador += 1

# somando os valores da lista
for i in lista_com_valores_multiplicados:
    soma += int(i)

# operações necessárias
resultado = (soma * 10) % 11

# obtendo o dígito 
segundo_digito = resultado if resultado <= 9 else 0

print(f'Primeiro dígto: {primeiro_digito} ')
print(f'Segundo dígito: {segundo_digito}')
