
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
#print(lista_numero_filmes)
#for item in lista_dicionarios:
    #print(item)

#################      Etapa - 1     #######################
for dicionario in lista_dicionarios:
    if 'numero_filmes_ator' in dicionario:
        numero_filmes = dicionario['numero_filmes_ator']
        if numero_filmes.isdigit():  # Verifique se é um número
            numero_filmes = int(numero_filmes)
            if numero_filmes > maiorQuant:
                maiorQuant = numero_filmes
                list_atorescommaisfilmes = [dicionario['ator']]
            elif numero_filmes == maiorQuant:
                list_atorescommaisfilmes.append(dicionario['ator'])
print(f'Ator(es) com o maior número de filmes: {list_atorescommaisfilmes}')
print(f'Número de filmes: {maiorQuant}')
with open('etapa-1.txt', mode='w') as arquivo:
    # Escreve no arquivo etapa-1.txt e fecha o objeto de arquivo
    arquivo.write(f'Ator(es) com o maior número de filmes: {list_atorescommaisfilmes}\n')
    arquivo.write(f'Número de filmes: {maiorQuant}')

#################      Etapa - 2    #######################
    
soma_gross = 0
    #variável para contar o número de valores da coluna 'Gross'
numero_de_valores = 0
    # Pula a primeira linha (cabeçalho)
for dicionario in lista_dicionarios[1:]:
    colunas = linha.strip().split(',')
    if len(colunas) >= 6:  
        valor_gross = colunas[5].strip().replace('$', '').replace(',', '')
        try:
            valor_gross = float(valor_gross) 
            soma_gross += valor_gross
            numero_de_valores += 1
        except ValueError:
            pass  
if numero_de_valores > 0:
    media_gross = soma_gross / numero_de_valores
    print("Média da coluna 'Gross':", media_gross)
else:
    print("Nenhum valor válido na coluna 'Gross'.")
with open('etapa-2.txt', mode='w') as arquivo:
    # Escreve no arquivo etapa-2.txt e fecha o objeto de arquivo
    arquivo.write(f'Média da coluna "Gross": {media_gross}')

#################      Etapa - 3    #######################

# Abre o arquivo CSV para leitura
with open('actors.csv', mode='r', newline='') as arquivo:
    linhas = arquivo.readlines()

    # Inicializa variáveis para armazenar o nome e a maior média de receita bruta por filme
    maior_media_receita = 0
    nome_maior_media = ""

    # Pula a primeira linha (cabeçalho)
    for linha in linhas[1:]:
        colunas = linha.strip().split(',')
        if len(colunas) >= 4:  # Certifique-se de que há pelo menos 4 colunas (incluindo 'Average per Movie')
            nome = colunas[0].strip()
            media_receita = colunas[3].strip().replace(',', '')  # Remove vírgulas
            if media_receita:  # Verifica se o valor é válido
                try:
                    media_receita = float(media_receita)  # Converte para float
                    if media_receita > maior_media_receita:
                        maior_media_receita = media_receita
                        nome_maior_media = nome
                except ValueError:
                    pass  # Ignora valores que não podem ser convertidos para float

    # Exibe o ator/atriz com a maior média de receita bruta por filme
    if nome_maior_media:
        print(f"{nome_maior_media} tem a maior média de receita bruta por filme: {maior_media_receita}")
    else:
        print("Nenhum valor válido encontrado para a média de receita bruta por filme.")


#################      Etapa - 4    #######################
# Abre o arquivo CSV para leitura
with open('actors.csv', mode='r', newline='') as arquivo:
    linhas = arquivo.readlines()

    # Inicializa um dicionário para contar as aparições de filmes
    contagem_filmes = {}

    # Pula a primeira linha (cabeçalho)
    for linha in linhas[1:]:
        colunas = linha.strip().split(',')
        if len(colunas) >= 6:  # Certifique-se de que há pelo menos 6 colunas (incluindo '#1 Movie')
            filme = colunas[4].strip()  # Obtém o nome do filme corretamente
            if filme:  # Verifica se o valor é válido
                if filme in contagem_filmes:
                    contagem_filmes[filme] += 1
                else:
                    contagem_filmes[filme] = 1

    # Ordena os filmes por quantidade de aparições (decrescente) e, em segundo nível, por nome do filme
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    # Escreve os resultados no arquivo de saída
    with open('etapa-4.txt', mode='w') as arquivo_saida:
        for sequencia, (filme, quantidade) in enumerate(filmes_ordenados, start=1):
            linha_saida = f"{sequencia} - O filme {filme} aparece {quantidade} vez(es) no dataset"
            arquivo_saida.write(linha_saida + '\n')
            print(linha_saida)