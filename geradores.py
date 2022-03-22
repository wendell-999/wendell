
### os geradores trabalham com otimizaçao de memoria 
## onde nao eh nescessario carregar todos os elementos na memoria da funçao ou da estrutura de dados 
# ou da estrutura de dados 

### criar uma funçao normal sem ser a geradora

import time 

def funcgerador():
    l = []
    for n in range(50):
        l.append(n)
        time.sleep(0,1)
    return l 

# jogando a funçao em memoria 
gen1 = funcgerador


"""
def funcgerador1():
    for in range(100):
        yield n 
        time.sleep(0,1)

"""


