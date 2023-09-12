class Aviao():
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.velocidade_maxima = velocidade_maxima
        self.modelo = modelo
        self.cor = 'azul'
        self.capacidade = capacidade

def main():
    lista = []
    avA = Aviao('BOIENG456', 1500, 400)
    avB = Aviao('Embraer Praetor 600', 863, 14)
    avC = Aviao('Antonov An-2', 258, 12)
    lista.append(avA)
    lista.append(avB)
    lista.append(avC)
    print(lista)
    for i in lista:
        print(f'modelo {i.modelo}: velocidade máxima {i.velocidade_maxima}: capacidade para {i.capacidade} passageiros: Cor {i.cor}')

main()