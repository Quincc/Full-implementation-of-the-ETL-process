#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, LongType, DoubleType, StringType, TimestampType

def main():
    spark = SparkSession.builder.appName("kafka-read-transactions-stream").getOrCreate()

    # Схема сообщения
    schema = StructType() \
        .add("transaction_id", LongType()) \
        .add("user_id", LongType()) \
        .add("amount", DoubleType()) \
        .add("currency", StringType()) \
        .add("status", StringType()) \
        .add("timestamp", TimestampType())

    # Чтение из Kafka
    kafka_df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "<FQDN_хоста>:9091") \
        .option("subscribe", "dataproc-kafka-topic") \
        .option("kafka.security.protocol", "SASL_SSL") \
        .option("kafka.sasl.mechanism", "SCRAM-SHA-512") \
        .option("kafka.sasl.jaas.config",
                "org.apache.kafka.common.security.scram.ScramLoginModule required "
                "username='user1' "
                "password='password1';") \
        .option("startingOffsets", "earliest") \
        .load()

    # Преобразование: извлечение JSON
    parsed_df = kafka_df.selectExpr("CAST(value AS STRING) as json_string") \
        .select(from_json(col("json_string"), schema).alias("data")) \
        .select("data.*") \
        .filter(col("status") == "success")

    # Запись результата в Object Storage
    output_path = "s3a://dataproc-bucket/kafka-stream-cleaned-output"

    query = parsed_df.writeStream \
        .format("parquet") \
        .option("checkpointLocation", "s3a://dataproc-bucket/checkpoints/kafka-read") \
        .option("path", output_path) \
        .trigger(once=True) \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    main()
