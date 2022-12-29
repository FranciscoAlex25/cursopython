# dict.get('chave') - pega uma chave específica 

pessoas = {
    'nome': [], 
    'idade': [],
    'sexo': [],
    'cpf': []
}

def cadastrarPessoa(nome, idade, sexo, cpf):
    pessoas['nome'].append(nome)
    pessoas['idade'].append(idade)
    pessoas['sexo'].append(sexo)
    pessoas['cpf'].append(cpf)


def listarDados():
    for i in range(len(pessoas['nome'])):
        print(pessoas['nome'][i])
        print(pessoas['idade'][i])
        print(pessoas['sexo'][i])
        print(pessoas['cpf'][i])
        print(30 * '-')


while True:
    opc = int(input('CADASTRAR: (1) LISTAR (2): '))

    if opc == 1:
        nome = input('informe seu nome: ')
        idade = input('informe sua idade: ')
        sexo = input('informe seu sexo: ')
        cpf = input('informe seu cpf: ')

        cadastrarPessoa(nome, idade, sexo, cpf)
    elif opc == 2:
        listarDados()
    else:
        break
