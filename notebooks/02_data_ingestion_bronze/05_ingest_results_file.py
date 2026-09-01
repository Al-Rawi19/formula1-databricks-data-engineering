# Databricks notebook source
# MAGIC  %run ../00-common/env-config

# COMMAND ----------

# MAGIC %run ../00-common/bronze-functions

# COMMAND ----------

# Define source_file and table_name
source_folder = f"{landing_folder_path}/results"
table_name = f"{catalog_name}.{bronze_schema}.results"

# COMMAND ----------

# Define the schema
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType

results_schema = StructType([
    StructField("date", DateType()),
    StructField("raceName", StringType()),
    StructField("round", IntegerType()),
    StructField("season", IntegerType()),
    StructField("url", StringType()),
    StructField("constructorId", StringType()),
    StructField("driverId", StringType()),
    StructField("grid", IntegerType()),
    StructField("laps", IntegerType()),
    StructField("number", IntegerType()),
    StructField("points", FloatType()),
    StructField("position", IntegerType()),
    StructField("positionText", StringType()),
    StructField("status", StringType())
])

# COMMAND ----------

# Read data from the results file
results_df = (
    spark.read
       .format('json')
       .schema(results_schema)
       .option('mode', 'FAILFAST')
       .load(source_folder)
)

# COMMAND ----------

results_final_df = add_ingestion_metadata(results_df)

# COMMAND ----------

(
    results_final_df
        .write
        .format('delta')
        .mode('overwrite')
        .saveAsTable(table_name)
)