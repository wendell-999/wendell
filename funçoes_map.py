#### funçao map aplica uma açao em uma estrutura de dados 
### e retorna os elementos com a açao aplicada

### primeiro elemento os

lista = [1,2,3,4,5,6]

def soma(x):
    return x+2

print(list(map(soma,lista)))