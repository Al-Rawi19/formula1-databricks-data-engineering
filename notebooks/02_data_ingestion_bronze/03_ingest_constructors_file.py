# Databricks notebook source
# MAGIC  %run ../00-common/env-config

# COMMAND ----------

# MAGIC %run ../00-common/bronze-functions

# COMMAND ----------

# Define source_file and table_name
source_file = f"{landing_folder_path}/constructors.json"
table_name = f"{catalog_name}.{bronze_schema}.constructors"

# COMMAND ----------

# Define the schema
constructors_schema = """constructorId STRING, 
                         name STRING, 
                         nationality STRING, 
                         url STRING
                         """

# COMMAND ----------

# Read data from the constructors file
constructors_df = (
    spark.read
       .format('json')
       .schema(constructors_schema)
       .option('mode', 'FAILFAST')
       .load(source_file)
)

# COMMAND ----------

constructors_final_df = add_ingestion_metadata(constructors_df)

# COMMAND ----------

(
    constructors_final_df
        .write
        .format('delta')
        .mode('overwrite')
        .saveAsTable(table_name)
)