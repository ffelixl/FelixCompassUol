import csv

if __name__ == '__main__':
    animais = ['Cachorro', 'Elefante', 'Zebra', 'Leão', 'Tigre', 'Coelho', 'Gato', 'Peixe', 'Pássaro', 'Borboleta', 'Golfinho', 'Rinoceronte', 'Orangotango', 'Tubarão', 'Cobra', 'Urso', 'Pinguim', 'Hipopótamo', 'Tartaruga', 'Macaco']
    animais.sort()
    
    for animal in animais:
        print(animal)

    with open('animais.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
    
        # Escrever cada animal em uma linha
        for animal in animais:
            escrever.writerow([animal])