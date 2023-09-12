def teste(*args, **kwargs):
    for i in args:
        print(i)
    for chave, valor in kwargs.items():
        print(valor)

teste(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x = 20)