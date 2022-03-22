#### objetos interaveis 
## estrutura de dados listas tuplas dicionarios strings 
## sao objetos interaveis
# exemplo 

lista = ["joao",1,"pedro",45]

#### como cheacar c o elemento eh interavel

## metodos magicos dados
#sao funçoes builtins do python onde sao escritas em formato de dunder ou duplo underline __ 
### metodo __iter__

### estou abrindo a caixinha do for 

### checar c um elemento eh interavel 
## hassattr checa o atributo de um elemento 

print(hasattr(lista,"__iter__"))

string = "florianopolis"

print(hasattr(string,"__iter__"))

### executando um interador a um interavel 

for s in string :
    print(s)

###  entender o proscesso dos interadores 

# metodo nao magico chamada iter 

### a funçao iter transforma um objeto interavel em interador 

listainterdor = iter(string)

print(type(listainterdor))

### ultilizar metodo magico "__next__" itera os elementos de memoria 

print(hasattr(listainterdor,"__next__"))

## interar a memoria 

print(next(listainterdor))
print(next(listainterdor))
print(next(listainterdor))
print(next(listainterdor))
print("separador de texto ")

for i in listainterdor:
    print(i)

