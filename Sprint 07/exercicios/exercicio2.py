##etapa 1 - baixar readme.md - wget https://raw.githubusercontent.com/ffelixl/FelixCompassUol/main/README.md?token=GHSAT0AAAAAACIHBGIE4ZYMFMSTJFK6WBQKZKKZIVA

##etapa 2 - app.py
import sys
from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":

        # Crie uma instância do SparkContext
        sc = SparkContext("local", "ContadorPalavras")

        # instância do SparkSession
        spark = SparkSession.builder.appName("ContadorPalavras").getOrCreate()

        text_rdd = sc.textFile("/home/jovyan/README.md?token=GHSAT0AAAAAACIHBGIE4ZYMFMSTJFK6WBQKZKKZIVA")

        # Divida o conteúdo em palavras e normalize as palavras (removendo pontuações e convertendo para minúsculas)
        words_rdd = text_rdd.flatMap(lambda line: line.split()).map(lambda word: word.strip('.,!?:;').lower())

        # Conte a ocorrência de cada palavra
        word_counts = words_rdd.countByValue()

        # Exiba as contagens das palavras
        for word, count in word_counts.items():
                print(f"{word}: {count}")

##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