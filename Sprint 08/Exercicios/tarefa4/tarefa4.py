from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.functions import lit, rand, when

# Criação da Spark Session
spark = SparkSession.builder.master("local[*]").appName("tarefa4").getOrCreate()

# Leitura do DataFrame e imprimir schema - passo 1 e 2
df_nomes = spark.read.csv("/home/ffelixl/nomes_aleatorios.txt", header=False)
df_nomes.show(5)
df_nomes.printSchema()
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.show(10)

#passo 3
# Adicionando uma nova coluna chamada 'Escolaridade' com valores aleatórios entre "fundamental", "medio" e "superior"
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() <= 0.33, lit("fundamental")).\
                                              when((rand() > 0.33) & (rand() <= 0.66), lit("medio")).\
                                              otherwise(lit("superior")))

#passo 4
# Lista de países da América do Sul
paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Chile", "Peru", "Venezuela", "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

# Adicionando uma nova coluna chamada 'Pais' com valores aleatórios entre os países da América do Sul
df_nomes = df_nomes.withColumn("Pais", lit("").cast("string")).\
    withColumn("Pais",
        when(rand() <= 1/13, paises_america_sul[0]).
        when(rand() <= 2/13, paises_america_sul[1]).
        when(rand() <= 3/13, paises_america_sul[2]).
        when(rand() <= 4/13, paises_america_sul[3]).
        when(rand() <= 5/13, paises_america_sul[4]).
        when(rand() <= 6/13, paises_america_sul[5]).
        when(rand() <= 7/13, paises_america_sul[6]).
        when(rand() <= 8/13, paises_america_sul[7]).
        when(rand() <= 9/13, paises_america_sul[8]).
        when(rand() <= 10/13, paises_america_sul[9]).
        when(rand() <= 11/13, paises_america_sul[10]).
        when(rand() <= 12/13, paises_america_sul[11]).
        otherwise(paises_america_sul[12]))

#passo 5
# Adicionando uma nova coluna chamada 'AnoNascimento' com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (lit(1945) + (rand() * 66)).cast("int"))

#passo 6
df_select = df_nomes.select("Nomes", "AnoNascimento").where(func.col("AnoNascimento") > 2000)
df_select.show(10)

#passo 7
df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select Nomes, AnoNascimento from pessoas where AnoNascimento > 2000").show(10)

#passo 8
df_nomes.select("Nomes", "AnoNascimento").where((func.col("AnoNascimento") > 1980) & (func.col("AnoNascimento") < 1994)).shhow(10)

#passo 9
spark.sql("select Nomes, AnoNascimento from pessoas where AnoNascimento between 1980 and 1994").show(10)

#passo 10
df_nomes = df_nomes.withColumn("Geracao",
    when((func.col("AnoNascimento") >= 1944) & (func.col("AnoNascimento") <= 1964), "Baby Boomers").
    when((func.col("AnoNascimento") >= 1965) & (func.col("AnoNascimento") <= 1979), "Geração X").
    when((func.col("AnoNascimento") >= 1980) & (func.col("AnoNascimento") <= 1994), "Millennials").
    when((func.col("AnoNascimento") >= 1995) & (func.col("AnoNascimento") <= 2015), "Geração Z").
    otherwise("Outra"))
df_nomes.show(10)
df_nomes.createOrReplaceTempView("pessoasgeracoes")
df_final = spark.sql("select Pais, Geracao, count(Nomes) as quantidade, sum(count(Nomes)) over() as somaTotal from pessoasgeracoes group by Pais, Geracao order by Pais, Geracao, quantidade")
df_final.show()

#caso eu quisesse converter o df pra pandas, só pra deixar registrado mesmo 
#pandas_df_resultado = df_final.toPandas()
# Exibindo o Pandas DataFrame resultante
#print("Pandas DataFrame Resultante:")
#print(pandas_df_resultado)