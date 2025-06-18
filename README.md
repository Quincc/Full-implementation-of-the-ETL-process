# 🚀 ETL-процесс на базе Yandex Cloud

## 📌 Описание

Этот проект реализует полный ETL-процесс с использованием облачной инфраструктуры **Yandex Cloud**. В процессе выполнены следующие этапы:

- Загрузка данных из YDB в Object Storage с помощью **Yandex DataTransfer**
- Обработка данных с помощью **PySpark** в **Yandex Data Processing**
- Автоматизация через **Apache Airflow**
- Потоковая обработка через **Apache Kafka**
- Визуальное подтверждение всех этапов

---

## ✅ Выполненные задания

### 🔹 Задание 1: Yandex DataTransfer (YDB → Object Storage)

📂 `task1/`
- `create_insert_transactions.yql` — создание таблицы и вставка данных в YDB
- `table.png` — подтверждение существования таблицы
- `transfer_success.png` — успешная передача данных в Object Storage

🛠️ Используемое:
- Yandex YDB
- YQL
- Yandex DataTransfer

---

### 🔹 Задание 2: PySpark + Apache Airflow + Data Processing

📂 `task2/`
- `create-table.py` — PySpark-задание по обработке данных (например, фильтрация по статусу)
- `Data-Processing-DAG.py` — DAG-файл, запускающий PySpark задание из Airflow
- `airflow_cluster.png` — созданный кластер DataProc
- `dags_success.png` — подтверждение успешного выполнения DAG

🛠️ Используемое:
- Yandex Data Processing (Spark)
- Apache Airflow
- Object Storage

---

### 🔹 Задание 3: Apache Kafka + PySpark

📂 `task3/`
- `kafka-read-batch.py` — пример чтения Kafka-сообщений пакетно
- `kafka-read-stream.py` — потоковое чтение Kafka
- `kafks-write.py` — запись данных в Kafka-топик

🛠️ Используемое:
- Yandex Managed Service for Apache Kafka
- PySpark Structured Streaming
- Kafka topics

---

## 🗂️ Структура репозитория

```
.
├── task1/
│   ├── create_insert_transactions.yql
│   ├── table.png
│   └── transfer_success.png
├── task2/
│   ├── create-table.py
│   ├── Data-Processing-DAG.py
│   ├── airflow_cluster.png
│   └── dags_success.png
├── task3/
│   ├── kafka-read-batch.py
│   ├── kafka-read-stream.py
│   └── kafks-write.py
└── README.md
```

---

## 🧰 Используемые технологии

- **Yandex Cloud**: YDB, DataTransfer, Data Processing, Object Storage, Apache Kafka
- **Apache Airflow**
- **Apache Spark (PySpark)**
- **Kafka Structured Streaming**
- **SQL/YQL/PySpark**

---

## 📎 Примечание

- Все скрипты и DAG-файлы готовы к развёртыванию в облаке
- Скриншоты подтверждают корректность выполнения заданий
