palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
palaInver = []
for palavracompleta in palavras:
    tamanhoPalavra = len(palavracompleta)
    #for para percorrer o tamanho da string de tras pra frente de cada palavra#
    for letra in range(tamanhoPalavra-1, 0-1, -1):
        palaInver.append(palavracompleta[letra])
    palavraInvertida = ''.join(palaInver) #Join para juntar as letras da lista que é a string invertida#
    if palavraInvertida == palavracompleta:
        print('A palavra: ' + palavraInvertida + ' é um palíndromo')
    else:
        print('A palavra: ' + palavracompleta + ' não é um palíndromo')
    palaInver = [] #esvaziando a lista para receber outra palavra depois que o for iterar#
        