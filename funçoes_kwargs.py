### permite passar um numero indeterminado de parametros para uma funçao 
## mas os parametros sao passados como indentificadores de chave e valor 
#a saida sera em formato de dicionario 


def saudaçao(**kwargs):
    print(kwargs)

saudaçao(manha ="bom dia", tarde = "boa tarde",noite = "boa noite")

def saudaçao_dia(**kwargs):
    for hora,saudaçao in kwargs.items():
        print(f"durante a {hora} dizemos {saudaçao}")

saudaçao_dia(manha ="bom dia")


## 2 underlines ou dunder quer dizer metodos magicos 
## _next_