import json

if __name__ == '__main__':
    arquivo = open('person.json')
    data = json.load(arquivo)
    print(data)