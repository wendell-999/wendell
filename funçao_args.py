### funçoes *args ultilizamos quando nao sabemos a quantidade exata de parametros 
## na funçao 
## *args retorna em tuplas 

def soma(*args):
    print(args)

soma (1,2,3,4,5,3,4,5,6,7,4,3,2,1,34,3)

def soma_total(*args):
    total = 0
    for numero in args:
        total = numero + total
    return total

print(soma_total(2,34,5,654,35))

