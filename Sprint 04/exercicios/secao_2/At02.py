def conta_vogais(palavra):
    palavra = palavra.lower()
    vogal = lambda c: c in 'aeiou'
    numerosVogais = len(list(filter(vogal, palavra)))
    return numerosVogais

