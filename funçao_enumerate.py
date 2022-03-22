## funçao enumerate retorna o indice de memoria de uma estruruta de dados 
# ex lista 

animais = ["cachorro","gato","passaro","elefante"]

print(list(enumerate(animais)))

### usar um interador ##

for i,valor in enumerate(animais):
    print(i,valor)

for i,valor in enumerate(animais):
    if i>1:
        break
    else:
        print(valor)


