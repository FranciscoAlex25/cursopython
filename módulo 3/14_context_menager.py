import os

caminho = os.path.dirname(__file__)

class MyOpen:
    def __init__(self, caminho, modo) -> None:
        print('inicializando')
        self.caminho = caminho
        self.modo = modo 
        self.arquivo = None 

    def __enter__(self):
        print('lendo arquivo')
        self.arquivo = open(self.caminho, self.modo, encoding='utf-8')
        return self.arquivo
    

    def __exit__(self, class_, exception_, traceback_):
        print('fechando arquivo')
        self.arquivo.close()


with MyOpen('caminho', 'w+') as arquivo:
    print('ENTER')
    arquivo.write('escrevendo algo muito grande')
