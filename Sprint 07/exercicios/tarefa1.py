import pandas as pd
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == "__main__":
    spark = SparkSession.builder.appName("teste").getOrCreate()
    arqschema = "Actor STRING, TotalGross FLOAT, NumberofMovies INT, AverageperMovie FLOAT, PMovie STRING, Gross FLOAT"
    csv = spark.read.csv(sys.argv[1], header=False, schema=arqschema)

    # Passo 2: Ler o arquivo CSV com o Pandas
    df = csv.toPandas()

    ator_mais_filmes = df.loc[df['NumberofMovies'].idxmax()]['Actor']
    numero_de_filmes = df['NumberofMovies'].max()

    # Passo 3: Realizar os cálculos solicitados
    # Calcula a média do número de filmes
    media_filmes = df['NumberofMovies'].mean()

    # Calcula a maior média por filme e apresenta o nome do ator/atriz correspondente
    maior_media_filme = df.loc[df['AverageperMovie'].idxmax()]['Actor']

    # Calcula o(s) filme(s) mais frequente(s) e sua respectiva frequência
    filmes_mais_frequentes = df['PMovie'].value_counts().head(1)

    # Passo 4: Apresentar as respostas
    print(f"Ator/atriz com o maior número de filmes: {ator_mais_filmes}")
    print(f"Número de filmes: {numero_de_filmes}")

    print(f"Média do número de filmes: {media_filmes}")

    print(f"Nome do ator/atriz com a maior média por filme: {maior_media_filme}")
    
    print(f"Filme(s) mais frequente(s) e sua respectiva frequência:\n{filmes_mais_frequentes}")

    spark.stop()
