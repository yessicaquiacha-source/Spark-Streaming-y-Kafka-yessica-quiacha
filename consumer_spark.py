from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Leer datos del topic de Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "datos_tiempo_real") \
    .load()

# Definir esquema
schema = StructType() \
    .add("usuario", StringType()) \
    .add("accion", StringType()) \
    .add("valor", IntegerType()) \
    .add("timestamp", StringType())

# Transformar los mensajes
json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Mostrar resultados en consola
query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()

# requirements.txt

pyspark
kafka-python
