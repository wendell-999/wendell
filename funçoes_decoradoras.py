### as funçoes decoradoras potencializam ou substituem a logica de fubcionamento de outra funçao 
## ou metodo


#### criando uma funçao decoradora

def master(msg):
    def imprime():
        
        print("essa eh a funçao pai, ou decoradora")
        msg()
    return imprime

#### segunda funçao que ira executar junto com a funçao decoradora

@master
def segunda_funçao():
    print("esta chamando a segunda funçao")


## executar as funçoes

segunda_funçao()

