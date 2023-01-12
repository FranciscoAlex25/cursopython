import os 

caminho = '/home/alex/Área de Trabalho/curso python/módulo 2/aula 30/arquivo.txt'

# arquivo = open(caminho, 'w')
# arquivo.close()

def exibir():
    arquivo.seek(0, 0)
    print(arquivo.read()) 


def voltar():
    arquivo.seek(0, 0)


with open(caminho, 'w+', encoding='utf-8') as arquivo:

    arquivo.write('coração' + '\n')
    arquivo.write('linha2' + '\n')
    arquivo.write('linha3' + '\n')

    arquivo.writelines(
        ('linha4\n', 'linha5\n', 'linha6\n')
    )

    voltar()
    for i in arquivo.readlines():
        print(i.strip())

# with open(caminho, 'r') as arquivo:
#     print(arquivo.read())
