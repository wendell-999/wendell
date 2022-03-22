#### lista eh uma estrutura de dados finita e ordenada 
#### possui indice de memoria. pode ser mutavel(adicionar,remover elementos)

# indice de memoria de uma estrutura de dados começa com 0

lista_inteiros = [12,23,543,13] 

lista_mista = ["morango",23,"uva","tomate",53]

print(lista_mista[2])

lista_mista.append(78)

print(lista_mista)

del lista_mista[1]

lista_mista.extend(lista_inteiros)

print(lista_mista)