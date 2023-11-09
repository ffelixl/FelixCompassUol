import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql import functions as F

# @params: [JOB_NAME, S3_INPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Lê o arquivo CSV do Amazon S3
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_catalog(database="glue-lab", table_name="catalogo").toDF()
# Converte a coluna "ano" para uma representação de string
df = df.withColumn("ano", df["ano"].cast("string"))
print("Esquema do DataFrame:")
df.printSchema()

# Define a função de transformação para alterar a caixa dos valores da coluna "nome" para maiúsculo
def transform_row(row):
    row["nome"] = row["nome"].upper()
    return row

# Aplica a transformação no DataFrame
df = df.withColumn("nome", F.upper(df["nome"]))

# Imprime a contagem de linhas no DataFrame
record_count = df.count()
print(f"Contagem de linhas no DataFrame: {record_count}")

# Realiza a contagem de nomes, agrupando por ano e sexo
grouped_df = df.groupBy(['ano', 'sexo']).agg(F.count('*').alias('count'))

# Ordena os dados pelo ano mais recente
sorted_df = grouped_df.orderBy(['ano'], ascending=[False])

# Imprime o DataFrame com a contagem de nomes (as 10 primeiras linhas)
sorted_df.show(10)

# Encontra o nome feminino com mais registros e em que ano ocorreu
max_female_name = df.filter(df['sexo'] == 'F').groupBy(['nome', 'ano']).agg(F.count('*').alias('count')).orderBy(['count'], ascending=[False]).first()
print(f"Nome feminino com mais registros: {max_female_name['nome']}, Ano: {max_female_name['ano']}")

# Encontra o nome masculino com mais registros e em que ano ocorreu
max_male_name = df.filter(df['sexo'] == 'M').groupBy(['nome', 'ano']).agg(F.count('*').alias('count')).orderBy(['count'], ascending=[False]).first()
print(f"Nome masculino com mais registros: {max_male_name['nome']}, Ano: {max_male_name['ano']}")

# Total de registros (masculinos e femininos) para cada ano
total_by_year = df.groupBy(['ano']).agg(F.count('*').alias('count')).orderBy(['ano'])
total_by_year.show()

output_path = args['S3_TARGET_PATH'] + "/frequencia_registro_nomes_eua/"
df.write.mode("overwrite").partitionBy("sexo", "ano").json(output_path)

print(f"Os dados foram gravados no S3 em: {output_path}")
