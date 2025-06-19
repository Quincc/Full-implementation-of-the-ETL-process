from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
from pyspark.sql.types import LongType, DoubleType, StringType
from pyspark.sql.utils import AnalysisException

# === Spark session ===
spark = SparkSession.builder.appName("Transactions ETL").getOrCreate()

# === Пути ===
source_path = "s3a://bucket-task-data/source-data/transactions_v2.csv"
target_path = "s3a://bucket-task-data/clean-data/transactions_v2.parquet"

try:
    print(f"Чтение данных из: {source_path}")
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(source_path)

    print("Схема исходных данных:")
    df.printSchema()

    # Приведение типов
    df = df.withColumn("transaction_id", col("transaction_id").cast(LongType())) \
           .withColumn("user_id", col("user_id").cast(LongType())) \
           .withColumn("amount", col("amount").cast(DoubleType())) \
           .withColumn("currency", col("currency").cast(StringType())) \
           .withColumn("status", col("status").cast(StringType())) \
           .withColumn("timestamp", to_timestamp(col("timestamp")))

    print("Схема после преобразования:")
    df.printSchema()

    # Фильтрация только успешных транзакций
    df = df.filter(col("status") == "success")

    # Удаление строк с null-значениями
    df = df.na.drop()

    print("Пример итоговых данных:")
    df.show(5)

    print(f"Запись в Parquet: {target_path}")
    df.write.mode("overwrite").parquet(target_path)

    print("✅ Успешно завершено.")

except AnalysisException as ae:
    print("❌ Ошибка анализа:", ae)
except Exception as e:
    print("❌ Общая ошибка:", e)

spark.stop()
