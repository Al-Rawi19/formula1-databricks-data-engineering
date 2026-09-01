# Databricks notebook source
# MAGIC  %run ../00-common/env-config

# COMMAND ----------

bronze_table = f"{catalog_name}.{bronze_schema}.constructors"
silver_table = f"{catalog_name}.{silver_schema}.constructors"

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

constructors_df = (
  spark.table(bronze_table)
       .drop("url")
       .withColumnsRenamed({
            "constructorId": "constructor_id",
            "name": "constructor_name"
        })
)

# COMMAND ----------

constructors_valid_df = (
    constructors_df
        .dropDuplicates(["constructor_id"])
)

# COMMAND ----------

constructors_final_df = (
    constructors_valid_df
        .withColumn('nationality', F.initcap(F.col("nationality")))
)

# COMMAND ----------

(
    constructors_final_df
        .write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(silver_table)
)