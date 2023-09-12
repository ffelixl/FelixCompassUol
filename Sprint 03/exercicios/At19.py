import random

random_list = random.sample(range(500), 4)
lista_ordenada = sorted(random_list)
tamanho_lista = len(lista_ordenada)

soma = sum(lista_ordenada)
if tamanho_lista % 2 != 0:
    mediana = lista_ordenada[int(tamanho_lista/2)]
else:
    mediana = (lista_ordenada[int(tamanho_lista/2-1)] + lista_ordenada[int(tamanho_lista/2)]) /2
media = soma/tamanho_lista
valor_maximo = max(lista_ordenada)
valor_minimo = min(lista_ordenada)
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')