# ETL-процесс с использованием Yandex Cloud

## 📝 Описание

Этот проект представляет собой реализацию полного ETL-процесса с использованием облачных сервисов **Yandex Cloud**, включая:
- Yandex DataTransfer
- Yandex Data Processing (Hadoop + Spark)
- Apache Airflow
- Apache Kafka
- DataLens для визуализации

---

## ✅ Выполненные задания

### 🔹 Задание 1: Работа с Yandex DataTransfer
- Создана база данных в **Yandex DataBase (YDB)**.
- Создана таблица `transactions_v2` с первичным ключом.
- Вставлены тестовые данные (15 строк).
- Настроен трансфер из YDB в **Object Storage** (формат — CSV/Parquet).
- Все YQL-скрипты сохранены в папке `ydb/`.

### 🔹 Задание 2: Обработка данных в Yandex Data Processing через Apache Airflow
- Подготовлены `.csv`-файлы с транзакциями.
- Написано PySpark-задание `process_transactions.py`:
  - Считывает данные из Object Storage
  - Фильтрует транзакции со статусом `"success"`
  - Сохраняет результат в Parquet
- Создан DAG `process_transactions_dag`:
  - Автоматически запускает PySpark задание на YDP
  - Управляется через Apache Airflow

### 🔹 Задание 3: Потоковая обработка Kafka + PySpark (**если выполнялось**)
- Настроен топик Kafka
- Написано PySpark-задание для потоковой обработки
- Использован кластер YDP

### 🔹 Задание 4 (доп): Визуализация в DataLens
- Построены дашборды на основе обработанных данных

---

## 🗂️ Структура проекта

```
etl_exa/
├── task1/
│   ├── create_table_transactions_v2.yql
│   └── insert_transactions_v2.yql
├── task2/
│   └── process_transactions.py
├── airflow/
│   └── process_transactions_dag.py
├── data/
│   └── transactions_01.csv
└── README.md
```

---

## ⚙️ Используемые технологии

- Yandex DataTransfer
- Yandex Data Processing (Spark)
- Apache Airflow
- Apache Kafka
- YDB
- HiveQL / SparkSQL / YQL
- DataLens

---

## 📌 Примечания

- Все ресурсы развёрнуты в рамках одного каталога Yandex Cloud
- Указаны сервисные аккаунты с нужными ролями (`ydb.editor`, `datatransfer.agent`, `airflow.admin`)
- Все задания выполнены в рамках лимитов бесплатного тарифа
