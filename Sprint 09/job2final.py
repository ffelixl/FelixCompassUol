from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import *
from urllib.request import urlopen, Request
from pyspark.sql.types import StringType, IntegerType, DateType
from pyspark.sql.functions import udf
import json


# Inicialização do contexto do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Carregamento de dados JSON do S3
bucket_name = "data-lake-do-felix"
file_paths = ["s3://{}/raw/tmdb/json/2023/11/16/file_1-5.json".format(bucket_name),
              "s3://{}/raw/tmdb/json/2023/11/16/file_6-10.json".format(bucket_name),
              "s3://{}/raw/tmdb/json/2023/11/16/file_11-15.json".format(bucket_name),
              "s3://{}/raw/tmdb/json/2023/11/16/file_16-20.json".format(bucket_name),
              "s3://{}/raw/tmdb/json/2023/11/16/file_21-25.json".format(bucket_name)]

json_df_list = [spark.read.json(file_path, multiLine=True) for file_path in file_paths]

# Imprimir o esquema do DataFrame
# json_df.printSchema()

# Selecionar colunas relevantes
selected_columns = ['id', 'genre_ids', 'title', 'original_language', 'original_title',
                     'popularity', 'release_date', 'overview', 'vote_count', 'vote_average']

# Criar um novo DataFrame apenas com as colunas selecionadas
dataframes = [json_df.select(selected_columns) for json_df in json_df_list]

def renomearcolunasdf(df):
    # Renomear as colunas
    column_mapping = {
        'id': 'ID',
        'genre_ids': 'ids_de_genero',
        'title': 'titulo',
        'original_language': 'linguagem_original',
        'original_title': 'titulo_original',
        'popularity': 'popularidade',
        'release_date': 'data_de_lancamento',
        'overview': 'overview',
        'vote_count': 'votos',
        'vote_average': 'media_de_votos'
    }

    # Aplicar a renomeação de colunas
    for old_col, new_col in column_mapping.items():
        df = df.withColumnRenamed(old_col, new_col)
    return df

dataframes = [renomearcolunasdf(df) for df in dataframes]

def verificardftemvaloresnulos(df):
    # Verificar valores nulos em cada coluna
    contagem_nulos_por_coluna = df.agg(*[sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])
    # Exibir a contagem de valores nulos por coluna
    contagem_nulos_por_coluna.show()

# Função para obter o ID do IMDb com base no ID do TMDb
def obter_id_imdb(tmdb_id):
    api_key = 'e32e0ce30c0a4728663eeada48d1c2cf'
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}/external_ids?api_key={api_key}&language=en-US'

    try:
        request = Request(url)
        response = urlopen(request)
        data = response.read().decode('utf-8')  # Leitura e decodificação do conteúdo da resposta
        json_data = json.loads(data)  # Análise do conteúdo como JSON

        imdb_id = json_data.get('imdb_id')
        return imdb_id
    except Exception as e:
        print(f"Erro ao obter ID do IMDb para o filme {tmdb_id}: {str(e)}")
        return None

# Função para adicionar a coluna IMDb ID ao DataFrame
def adicionar_coluna_imdb_id(df):
    obter_id_imdb_udf = udf(lambda tmdb_id: obter_id_imdb(tmdb_id), StringType())
    df_com_imdb = df.withColumn('imdb_id', obter_id_imdb_udf(df['id']))
    return df_com_imdb

# Adicionar a coluna IMDb ID
dataframes_com_imdb = [adicionar_coluna_imdb_id(df) for df in dataframes]

# Adicionar ação para garantir que as transformações sejam aplicadas
for df in dataframes_com_imdb:
    df.count()

# Exibir DataFrame com coluna IMDb ID
for i, df in enumerate(dataframes_com_imdb, start=1):
    print(f"DataFrame {i} com coluna IMDb ID:")
    df.show(truncate=False)

# Agrupar os dataframes em um só
df_union = dataframes_com_imdb[0]
for i in range(1, len(dataframes_com_imdb)):
    df_union = df_union.union(dataframes_com_imdb[i])

df_union.show(truncate=False)
verificardftemvaloresnulos(df_union)

# Filtrar as linhas onde imdb_id não é nulo
df_sem_nulos = df_union.filter(col("imdb_id").isNotNull())

# Alterar o tipo da coluna 'id' para IntegerType
df_sem_nulos = df_sem_nulos.withColumn("id", col("id").cast(IntegerType()))

# Alterar o tipo da coluna 'votos' para IntegerType
df_sem_nulos = df_sem_nulos.withColumn("votos", col("votos").cast(IntegerType()))

# Converter a coluna 'data_de_lancamento' para o tipo DateType
df_sem_nulos = df_sem_nulos.withColumn("data_de_lancamento", to_date(col("data_de_lancamento"), 'yyyy-MM-dd'))

# Exibir o DataFrame resultante
df_sem_nulos.show(truncate=False)

# Exibir a contagem de linhas do DataFrame
print("Contagem de Linhas do DataFrame:", df_sem_nulos.count())

# Escrever arquivo no formato parquet no S3
output_path = "s3://{}/trusted/parquetfilmestmdb/2023/11/16".format(bucket_name)
# Escrever os dados no Amazon S3
df_sem_nulos.write.parquet(output_path, mode="overwrite")