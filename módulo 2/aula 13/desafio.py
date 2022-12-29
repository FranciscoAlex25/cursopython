# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Qual destes é um exemplo de polissacarídeo?',
        'itens': ['glicose', 'sacarose', 'celulose', 'maltose'],
        'resposta': 'celulose'
    },
    {
        'pergunta': 'Qual a função da parede celular?', 
        'itens': ['isolar', 'regar', 'destruir', 'comprimir'], 
        'resposta': 'isolar'
    },
     {
        'pergunta': 'Qual a função dos ribossomos?', 
        'itens': ['sintetizar proteína', 'proteger as células', 'produzir lipídeos'], 
        'resposta': 'sintetizar proteína'
    }
]

acerto = 0 
escolha = '' 
index = 0 
item = ''

def perguntar():
    global escolha, acerto 

    # percorre todas as erguntas
    for questoes in perguntas:

        #percorre pergunta, item e resposta
        for chave, valor in questoes.items():
            if chave == 'pergunta':
                print()
                print(valor)
            if chave == 'itens':
                for itenss in valor:
                    index = valor.index(itenss)
                    print(f'{index}) {itenss}')

        item = input('Escolha um item: ') 
        
        # busca o item escolhido e verifica se acertou ou errou 
        for c, v in questoes.items():
            if c == 'itens':
                for itm in v:
                    if int(item) == v.index(itm):
                        escolha = itm
                        break

            if c == 'resposta':
                if escolha == questoes[c]:
                    acerto += 1 
                    print(f'{"Parabéns você acertou!"} 🤩')
                    break
                else:
                    print(f'{"Você errou, que pena!"} 😭')
                    break


perguntar()


print()
print(f'Você teve {acerto} acertos! ✅')
