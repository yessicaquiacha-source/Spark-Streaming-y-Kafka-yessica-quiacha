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
