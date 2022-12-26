'''
Faça um jogo para o usuário advinhar qual a palavra secreta.
Você vai propor a palavra secreta e vai dar a chance do usuário
apenas digitar uma letra. Quando o usuário digitar a letra você 
irá verificar se a letra está na palavra. Se a letra estiver na 
palavra, digite a letra, caso contrário, exiba *. 
Faça a contagem de tentativas do seu usuário.
'''

palavra = 'suco'
tentativas = 0 
tamanho_palavra = len(palavra)
frase = list(len(palavra) * '*')

print(frase)

while True:
    # Verifica se tem letras para advinhar 
    if '*' not in frase:
        print()
        break 
    # Verifica o número de tentativas e pede a letra ao usuário
    tentativas += 1
    letra = str(input('Digite uma letra: '))
    # Verifica se o usuario digitou mais de uma letra
    if len(letra) > 1:
        print('Digite apenas uma letra! ') 
    else:
        # Verifica se tem a letra digitada
        if letra in palavra:
            cont = 0
            # Percorre a palavra e procura a letra
            while cont < tamanho_palavra:
                if palavra[cont] == letra:
                    frase[cont] = letra
                cont += 1 
            # Exibe a palavra
            for i in frase:
                print(i, end=' ')
            print()
        else:
            # Exibe a palavra
            for i in frase:
                print(i, end=' ')
            print()

# Mensagem final
print(f'Parabéns, você acertou! Tentativas {tentativas}')
