# Databricks notebook source
# MAGIC  %run ../00-common/env-config

# COMMAND ----------

bronze_table = f"{catalog_name}.{bronze_schema}.drivers"
silver_table = f"{catalog_name}.{silver_schema}.drivers"

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

drivers_df = (
  spark.table(bronze_table)
       .drop(F.col("url"))
       .withColumnsRenamed({
            "driverId": "driver_id",
            "dateOfBirth": "date_of_birth"
        })
       .withColumn("driver_name", 
                   F.initcap(F.concat_ws(" ", F.col("name.givenName"), F.col("name.familyName"))))
       .drop("name")
)

# COMMAND ----------

drivers_valid_df = (
    drivers_df
        .dropDuplicates(["driver_id"])
)

# COMMAND ----------

drivers_final_df = (
    drivers_valid_df
        .withColumn('nationality', F.initcap(F.col("nationality")))
)

# COMMAND ----------

(
    drivers_final_df
        .write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(silver_table)
)