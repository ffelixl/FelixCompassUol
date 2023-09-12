
def quebra(lista):
    tamanhoLista = len(lista)
    partedivid = int(tamanhoLista/3)
    lista_a = lista[:partedivid]
    lista_b = lista[partedivid:partedivid*2]
    lista_c = lista[partedivid*2:tamanhoLista]
    return lista_a, lista_b, lista_c
    
listaTotal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista_a, lista_b, lista_c = quebra(listaTotal)
print(lista_a, lista_b, lista_c, end="")