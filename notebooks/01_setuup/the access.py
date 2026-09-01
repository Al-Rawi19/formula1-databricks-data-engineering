# Databricks notebook source
# create external location for access cloud storage data
%sql
CREATE EXTERNAL LOCATION IF NOT EXISTS `databricks_ingestion_exl`
    URL 's3://databrickks-demo-ingestion-formula1/'
    WITH (STORAGE CREDENTIAL `databricks_ingestion_cr`)
    COMMENT 'External S3 bucket path For Ingestion Data';


# COMMAND ----------

# MAGIC %sql SHOW CATALOGS

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS formula1
# MAGIC   MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/'
# MAGIC   COMMENT 'THIS IS THE MAIN CATALOG FOR FORMULA1 PROJECT'

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS formula1.landing;
# MAGIC CREATE SCHEMA IF NOT EXISTS formula1.bronze
# MAGIC     MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/bronze';
# MAGIC CREATE SCHEMA IF NOT EXISTS formula1.silver
# MAGIC     MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/silver';
# MAGIC CREATE SCHEMA IF NOT EXISTS formula1.gold
# MAGIC     MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/gold';    

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_catalog();

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG formula1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL VOLUME formula1.landing.files
# MAGIC LOCATION 's3://databrickks-demo-ingestion-formula1/landing';

# COMMAND ----------

# MAGIC %fs ls '/Volumes/formula1/landing/files'