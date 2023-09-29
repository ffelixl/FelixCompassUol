def pares_ate(n:int):
    for i in range(2, n+1, 2):
        yield i

valorDoIntervalo = int(input('Digite um numero para o intervalo\n'))
sequencia = pares_ate(valorDoIntervalo)
for i in sequencia:
    print(i)
