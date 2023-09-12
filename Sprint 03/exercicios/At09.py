
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (pnome, snome, idd) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {pnome} {snome} está com {idd} anos")