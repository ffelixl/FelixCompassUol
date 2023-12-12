import pandas as pd
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col, count, when
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Inicialização do contexto do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

schema = StructType([
    StructField("ator", StringType(), True),
    StructField("total_bruto", DoubleType(), True),
    StructField("numero_de_filmes", IntegerType(), True),
    StructField("media_por_filme", DoubleType(), True),
    StructField("primeiro_filme", StringType(), True),
    StructField("totalpfilme", DoubleType(), True),
])

# Carregamento de dados de atores do S3
bucket_name = "data-lake-do-felix"
file_path = "s3://{}/raw/dadosAtores/actors.csv"

# Ler o arquivo Excel para o Pandas
df = spark.read.csv(file_path, header=True, schema=schema)

# Exibir o DataFrame do Spark
df.show()

# Função para verificar valores nulos em cada coluna
def verificardftemvaloresnulos(df_spark):
        # Criar uma lista de expressões para contar valores nulos em cada coluna
    exprs = [count(when(col(c).isNull(), c)).alias(c) for c in df_spark.columns]

    # Aplicar as expressões para obter a contagem de nulos por coluna
    contagem_nulos_por_coluna = df_spark.agg(*exprs)

    # Exibir a contagem de valores nulos por coluna
    contagem_nulos_por_coluna.show()

verificardftemvaloresnulos(df)

# Escrever arquivo no formato parquet no S3
output_path = "s3://{}/trusted/parquetAtores/".format(bucket_name)
# Escrever os dados no Amazon S3 com coalesce(1) para ter um único arquivo
df.write.parquet(output_path, mode="overwrite")