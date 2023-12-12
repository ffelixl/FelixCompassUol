from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pandas as pd
from IPython.display import display

# Inicialização do contexto do Spark e Glue
# sc = SparkContext()
# glueContext = GlueContext(sc)
spark = SparkSession.builder.appName("testetrusted").getOrCreate()

# Carregamento de dados JSON
json_df1 = spark.read.json("/home/ffelixl/file_1-5.json", multiLine=True)
json_df2 = spark.read.json("/home/ffelixl/file_6-10.json", multiLine=True)
json_df3 = spark.read.json("/home/ffelixl/file_11-15.json", multiLine=True)
json_df4 = spark.read.json("/home/ffelixl/file_16-20.json", multiLine=True)
json_df5 = spark.read.json("/home/ffelixl/file_21-25.json", multiLine=True)

# Imprimir o esquema do DataFrame
#json_df.printSchema()

# Selecionar colunas relevantes
selected_columns = ['id', 'genre_ids', 'title', 'original_language', 'original_title',
                     'popularity', 'release_date', 'overview', 'vote_count', 'vote_average']

# Criar um novo DataFrame apenas com as colunas selecionadas
df1 = json_df1.select(selected_columns)
df2 = json_df2.select(selected_columns)
df3 = json_df3.select(selected_columns)
df4 = json_df4.select(selected_columns)
df5 = json_df5.select(selected_columns)


def renomearcolunasdf(df):
        # Renomear as colunas
        column_mapping = {
                'id': 'ID',
                'genre_ids': 'IDs de genero',
                'title': 'Titulo',
                'original_language': 'linguagem original',
                'original_title': 'Titulo original',
                'popularity': 'Popularidade',
                'release_date': 'Data de lancamento',
                'overview': 'Overview',
                'vote_count': 'Votos',
                'vote_average': 'Media de votos'
        }

        # Aplicar a renomeação de colunas
        for old_col, new_col in column_mapping.items():
                df = df.withColumnRenamed(old_col, new_col)
        return df
df1 = renomearcolunasdf(df1)
df2 = renomearcolunasdf(df1)
df3 = renomearcolunasdf(df1)
df4 = renomearcolunasdf(df1)
df5 = renomearcolunasdf(df1)

def verificardftemvaloresnulos(df):
        # Verificar valores nulos em cada coluna
        contagem_nulos_por_coluna = df.agg(*[sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])
        # Exibir a contagem de valores nulos por coluna
        contagem_nulos_por_coluna.show()

verificardftemvaloresnulos(df1)
verificardftemvaloresnulos(df2)
verificardftemvaloresnulos(df3)
verificardftemvaloresnulos(df4)
verificardftemvaloresnulos(df5)

# Exibir DataFrame com colunas renomeadas
df1.show(truncate=False)
df2.show(truncate=False)
df3.show(truncate=False)
df4.show(truncate=False)
df5.show(truncate=False)