idade = [12, 21, 32, 10, 9, 8, 9]

def mediaIdade(*args):
    soma = sum(args)
    media = round((soma / len(idade)), 2)
    
    return media

resultado = mediaIdade(*idade)

print(resultado)
