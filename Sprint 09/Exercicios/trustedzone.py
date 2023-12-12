from pyspark.context import SparkContext
#from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Inicialização do contexto do Spark e Glue
#sc = SparkContext()
#glueContext = GlueContext(sc)
spark = SparkSession.builder.appName("testetrusted").getOrCreate()

# Carregamento de dados JSON
json_df = spark.read.json("C:/Users/franc/OneDrive/Área de Trabalho/Sprint09/Exercicios/file_21-25.json", multiLine=True)

# Imprimir o esquema do DataFrame
json_df.printSchema()

# Transformações necessárias (Exemplo)
#transformed_df = source_df.parquet
#print(transformed_df)

# Escrita dos dados na Trusted Zone
#transformed_df.write.mode("overwrite").parquet("s3://caminho/para/trusted/zone/csv")

# Exemplo de job 2 (TMDB) pode seguir uma estrutura similar, mas com diferentes transformações e caminhos.

# Fim do job
#job.commit()
