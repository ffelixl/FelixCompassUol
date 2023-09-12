class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada
    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse = True)
        return self.listaBaguncada

def main():
    lista_a = [3,4,2,1,5]
    lista_b = [9,7,6,8]
    crescente = Ordenadora(lista_a)
    decrescente = Ordenadora(lista_b)
    print(crescente.ordenacaoCrescente())
    print(decrescente.ordenacaoDecrescente())


main()