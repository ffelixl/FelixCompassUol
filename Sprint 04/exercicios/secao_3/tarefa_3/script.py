import hashlib

def calcular_sha1_hash(texto):
    sha1 = hashlib.sha1()
    sha1.update(texto.encode('utf-8'))
    return sha1.hexdigest()

if __name__ == "__main__":
    while True:
        texto = input("Digite a string para mostrar seu hash: ")
        hash_sha1 = calcular_sha1_hash(texto)
        print("Hash SHA-1 da string:", hash_sha1)
        verifi = input("Digite 1 para digitar nova string ou 2 para sair do programa\n")
        if int(verifi) == 1:
            pass
        elif int(verifi) == 2:
            break
        else:
            print("Comando invalido")


