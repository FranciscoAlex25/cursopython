x, z = 1, 4

def imprimir():
    global z
    x = 3
    print(x, z)
    def imprimir2():
        y = 2
        print(x, y)
    
    imprimir2()


print(x)
imprimir()
