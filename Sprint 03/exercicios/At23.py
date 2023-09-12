class Calculo:
    def soma(x, y):
        return x + y
    
    def subtracao(x, y):
        return x - y
    
a = 4 
b = 5
resulSoma = Calculo.soma(a, b)
resulSub = Calculo.subtracao(a, b)
print(f'Somando: {resulSoma}')
print(f'Subtraindo: {resulSub}')
