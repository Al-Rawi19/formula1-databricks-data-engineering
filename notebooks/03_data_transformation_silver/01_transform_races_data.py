# Databricks notebook source
# MAGIC  %run ../00-common/env-config

# COMMAND ----------

bronze_table = f"{catalog_name}.{bronze_schema}.races"
silver_table = f"{catalog_name}.{silver_schema}.races"

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

races_df = (
  spark.table(bronze_table)
       .select(
            F.col("season"),
            F.col("round"),
            F.col("raceName"),
            F.col("date"),
            F.col("circuitId"),
            F.col("ingestion_timestamp"),
            F.col("source_file")
        )
       .withColumnsRenamed({
            "circuitId": "circuit_id",
            "raceName": "race_name",
            "date": "race_date"
        })
)

# COMMAND ----------

races_valid_df = (
    races_df
        .dropDuplicates(["season","round"])
)

# COMMAND ----------

races_final_df = (
    races_valid_df
        .withColumn('race_name', F.initcap(F.col("race_name")))
)

# COMMAND ----------

(
    races_final_df
        .write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(silver_table)
)