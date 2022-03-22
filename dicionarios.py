#### dicionarios é uma coleçao desordenada de objetos 
# representado por chaves
# o dicionario ultiliza um formato json

### exemplo de dicionarios 

dic01 = {"chave": "valor"}

estados_siglas = {"sc":"santa catarina","pr":"parana",
"rs":"rio grande do sul","sp":"sao paulo"}

print(estados_siglas)


for d in estados_siglas.values():
    print(d)

for d in estados_siglas.keys():
    print(d)

