# Proyecto Spark Streaming con Kafka
Este proyecto implementa un flujo de procesamiento de datos en tiempo real usando **Apache Kafka** y **Apache Spark Streaming**.

## Objetivo
Simular el envío de datos desde un productor Kafka y procesarlos en tiempo real con Spark Streaming, aplicando limpieza y análisis básico.

## Componentes
- `producer.py`: Genera datos simulados y los envía a Kafka.
- `consumer_spark.py`: Recibe los datos desde Kafka y los procesa con Spark.
- `dataset/datos_ejemplo.csv`: Datos base para pruebas.

## Ejecución
1. Iniciar Zookeeper y Kafka:
   ```bash
   ./bin/zookeeper-server-start.sh config/zookeeper.properties
   ./bin/kafka-server-start.sh config/server.properties

## Crear un topic en Kafka
./bin/kafka-topics.sh --create --topic datos_tiempo_real --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

## Ejecutar el productor
python3 producer.py

## Ejecutar el consumidor (Spark Streaming)
spark-submit consumer_spark.py

---

### 🧩 **`producer.py`**
Genera datos falsos y los envía al *topic* de Kafka.


### python
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        'usuario': random.choice(['Carlos', 'Ana', 'Luis', 'María']),
        'accion': random.choice(['login', 'logout', 'compra', 'busqueda']),
        'valor': random.randint(1, 500),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    producer.send('datos_tiempo_real', data)
    print(f"Evento enviado: {data}")
    time.sleep(2)

    
