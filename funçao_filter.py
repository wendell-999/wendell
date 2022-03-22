
## funçao filter filtra e separa um elemento solicitado trazendo a saida


lista_mista = [1,"wendell",34,"janeiro",13]

def valida(x):
    return x == "joao"

print(list(filter(valida,lista_mista)))

