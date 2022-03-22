##### funçoes sao pequenos pedaços de codigo definidos 
#### para executar determinada açao;
### as funçoes servem para executar toda vez que uma açao 
## e solicitada. otimizando linhas de codigo e tempo de execuçao .
# evitando linhas de codigos repetitivas.

# funçao sem argumento

def oi():
    print("ola pessoal")

## chamando a funçao 

oi()

## funçao com argumento 

def soma(x,y):
    return x+y


### chamar a funçao 

s = soma(2,3)

print(s)


def testa_nome(nome,idade):
    print(f"ola {nome} sua idade é : {idade} ")


testa_nome("wendell",15)

