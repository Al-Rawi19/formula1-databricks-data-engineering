# Databricks notebook source
# MAGIC  %run ../00-common/env-config

# COMMAND ----------

bronze_table = f"{catalog_name}.{bronze_schema}.circuits"
silver_table = f"{catalog_name}.{silver_schema}.circuits"

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

circuits_df = (
  spark.table(bronze_table)
       .select(
                F.col("circuitId"),
                F.col("circuitName"),
                F.col("lat"),
                F.col("long"),
                F.col("locality"),
                F.col("country"),
                F.col("ingestion_timestamp"),
                F.col("source_file")
        )
       .withColumnsRenamed({
            "circuitId": "circuit_id",
            "circuitName": "circuit_name",
            "lat": "latitude",
            "long": "longitude"
        })
)

# COMMAND ----------

circuits_valid_df = (
    circuits_df
        .filter(
            F.col("circuit_id").isNotNull()
        )
)

# COMMAND ----------

circuits_final_df = (
    circuits_valid_df
        .withColumn('circuit_name', F.initcap(F.col("circuit_name")))
        .withColumn('locality', F.initcap(F.col("locality")))
)

# COMMAND ----------

(
    circuits_final_df
        .write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(silver_table)
)