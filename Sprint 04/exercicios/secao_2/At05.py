import csv

def processar_arquivo(nome_arquivo):
    dados_processados = []

    with open(nome_arquivo, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            nome = linha[0]
            notas = list(map(int, linha[1:])) #criacao de uma lista com todas as notas do aluno
            tresMaioresNotas = sorted(notas, reverse=True)[:3] #Pegando as 3 maiores notas
            mediaMaioresNotas = round(sum(tresMaioresNotas) / len(tresMaioresNotas), 2)
            resultado_estudante = f"Nome: {nome} Notas: {tresMaioresNotas} Média: {mediaMaioresNotas}"
            dados_processados.append(resultado_estudante)

    dados_processados.sort()
    for resultado in dados_processados:
        print(resultado)

processar_arquivo('estudantes.csv')
