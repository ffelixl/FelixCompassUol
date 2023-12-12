from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import *
import pandas as pd
from setuptools import setup
from pyspark.sql.types import IntegerType

setup(
    name='MyJob',
    install_requires=[
        'openpyxl==3.0.14',  # Substitua a versão pela versão específica que você precisa
        # Adicione outras dependências, se necessário
    ],
)

# Inicialização do contexto do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Carregamento de dados de oscars do S3
bucket_name = "data-lake-do-felix"
file_path = "s3://{}/raw/dadosOscars/Dados_oscar.xlsx".format(bucket_name)

df = pd.read_excel(file_path)  # lendo o arquivo xlsx para o pandas
df_spark = spark.createDataFrame(df)  # criando um dataframe do spark
df_spark.show()

# Função para verificar valores nulos em cada coluna
def verificardftemvaloresnulos(df_spark):
    # Criar uma lista de expressões para contar valores nulos em cada coluna
    exprs = [count(when(col(c).isNull(), c)).alias(c) for c in df_spark.columns]

    # Aplicar as expressões para obter a contagem de nulos por coluna
    contagem_nulos_por_coluna = df_spark.agg(*exprs)

    # Exibir a contagem de valores nulos por coluna
    contagem_nulos_por_coluna.show()

# Chamar a função para verificar valores nulos
verificardftemvaloresnulos(df_spark)

# Função para renomear colunas
def renomearcolunasdf(df_spark):
    # Renomear as colunas
    column_mapping = {
        'Film Year': 'ano_filme',
        'Ceremony Year': 'ano_cerimonia',
        'Category': 'categoria',
        'Name': 'nome',
        'Film': 'filme',
        'Status': 'status',
    }
    # Aplicar a renomeação de colunas
    for old_col, new_col in column_mapping.items():
        df_spark = df_spark.withColumnRenamed(old_col, new_col)

    # Retornar o DataFrame renomeado
    return df_spark

# Chamar a função para renomear colunas
df_colunas_renomeadas = renomearcolunasdf(df_spark)
df = df_colunas_renomeadas.withColumn("ano_filme", df_colunas_renomeadas["ano_filme"].cast(IntegerType()))
df = df.withColumn("ano_cerimonia", df["ano_cerimonia"].cast(IntegerType()))
df.show()
df.printSchema()
# Escrever arquivo no formato parquet no S3
output_path = "s3://{}/trusted/parquetOscars/".format(bucket_name)
# Escrever os dados no Amazon S3
df.write.parquet(output_path, mode="overwrite")

