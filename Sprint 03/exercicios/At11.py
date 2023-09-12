arquivo = open('arquivo_texto.txt', mode='r', encoding='ISO 8859-1')
conteudo = arquivo.read()
print(conteudo, end="")