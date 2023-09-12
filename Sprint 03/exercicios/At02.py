
numeros = []
for i in range(0, 3):
    a = input(f'Digite o {i+1}° numero\n')
    numeros.append(a)
    if int(numeros[i]) % 2 == 0:
        print(f'Par: {numeros[i]}')
    else:
        print(f'Ímpar: {numeros[i]}')