# Databricks notebook source
# import common enviroment configuration
 %run ../00-common/env-config

# COMMAND ----------

# import common bronze functions
%run ../00-common/bronze-functions

# COMMAND ----------

# define source file and table name
source_file = f"{landing_folder_path}/circuits.csv"
table_name = f"{catalog_name}.{bronze_schema}.circuits"

# COMMAND ----------

# define schema
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
circuits_schema = StructType ([
    StructField('circuitId',       StringType()),
    StructField('url',             StringType()),
    StructField('circuitName',     StringType()),
    StructField('lat',             DoubleType()),
    StructField('long',            DoubleType()),
    StructField('locality',        StringType()),
    StructField('country',         StringType())
])

# COMMAND ----------

# read data from source file
circuits_df = (
    spark.read
        .format('csv')
        .option('header', True)
        .option('mode', 'FAILFAST')
        .schema(circuits_schema)
        .load(source_file)
)

# COMMAND ----------

circuits_final_df = add_ingestion_metadata(circuits_df)

# COMMAND ----------

# save data to table
(
    circuits_final_df
        .write
        .mode('overwrite')
        .format('delta')
        .saveAsTable(table_name)
)