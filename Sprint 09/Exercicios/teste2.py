
from pyspark.sql import SparkSession

# Inicializar uma sessão Spark
spark = SparkSession.builder.appName("LeituraParquet").getOrCreate()

# Caminho para o arquivo Parquet
caminho_parquet = "/home/ffelixl/arquivosparquet/files.parquet"

# Ler o arquivo Parquet para um DataFrame
df_parquet = spark.read.parquet(caminho_parquet)

# Mostrar a tabela
df_parquet.show()
df_parquet.select("title", "release_date", "vote_average").show()

# Encerrar a sessão Spark
spark.stop()

