import random

if __name__ == '__main__':
    numeros = [random.randint(1, 1000) for _ in range(250)]
    #print(numeros)
    numeros.reverse()
    print(numeros)
