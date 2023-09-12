
arquivo = open('actors.csv', mode='r')
conteudo = arquivo.read()
sepLinhas = conteudo.splitlines()
tamanho_linhas = len(sepLinhas)
#print(tamanho_linhas)
chaves = ['ator', 'Receitas_filme_ator', 
          'numero_filmes_ator', 'media_por_quantidade_de_filme', 
          'filme_com_maior_receita', 'receita_bruta_filme_maior_receita']
lista_dicionarios = []
lista_numero_filmes = []
list_atorescommaisfilmes = []
maiorQuant = 0
for linha in sepLinhas:
    b = linha.strip().replace("\t", "")
    c = b.strip('"')
    b = c.replace(', ', " ")
    b = b.replace('."', "")
    sepVirgulas = b.split(',')
    #print(sepVirgulas)
    dicionario = {}
    for indice, palavra in enumerate(sepVirgulas):
        if indice < len(chaves):
            if palavra:
                dicionario[chaves[indice]] = palavra
    lista_dicionarios.append(dicionario)
    if 'numero_filmes_ator' in dicionario:
        numero_filmes = dicionario['numero_filmes_ator']
        lista_numero_filmes.append(numero_filmes)
    lista_numero_filmes.remove["Number of Movies"]
    
print(lista_numero_filmes)
#for item in lista_dicionarios:
    #print(item)

        