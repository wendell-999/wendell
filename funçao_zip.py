
dicverduras = {1:"cebola",2:"alface",3:"repolho",4:'beterraba'}
dicfrutas = {1:'maça',2:'laranja',3:'pera'}


junta = list(zip(dicverduras.items(),dicfrutas.items()))

print(junta)

for p in junta:
    print(p)