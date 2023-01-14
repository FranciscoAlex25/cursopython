class CarrinhoCompras:
    def __init__(self):
        self._produtos = []

    def cadastrar_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    
    def somar_produto_preco(self):
        preco = sum([produto.preco for produto in self._produtos])
        return preco
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(vars(produto))
        return ''


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco 


carrinho = CarrinhoCompras()
produto_1, produto_2, produto_3 = Produto('arroz', 8), Produto('carne', 20), Produto('suco', 2.50)

carrinho.cadastrar_produtos(produto_1, produto_2, produto_3)

print(carrinho.listar_produtos())
print(carrinho.somar_produto_preco())
