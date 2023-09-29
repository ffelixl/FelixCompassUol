def processar_arquivo():
    arquivo = open('number.txt')
    conteudo = arquivo.readlines()
    valores = list(map(int, conteudo))
    return valores

def ordenarlista(valores):
    return sorted(valores)

def somarnumeros(valores):
    soma = sum(valores)
    return soma

def filtrarPares(valores):
    var = filter(lambda v: v % 2 == 0, valores)
    return list(var)


lista = processar_arquivo()
lista = filtrarPares(lista)
lista = ordenarlista(lista)
lista = list(reversed(lista))[:5]
soma = somarnumeros(lista)
print(lista)
print(soma)

    
    