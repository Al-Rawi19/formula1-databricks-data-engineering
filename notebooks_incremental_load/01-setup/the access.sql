-- Databricks notebook source
CREATE EXTERNAL LOCATION IF NOT EXISTS `databricks_ingestion_incremental_load_exl`
    URL 's3://databrickks-demo-ingestion-formula1/'
    WITH (STORAGE CREDENTIAL `databricks_ingestion_cr`)
    COMMENT 'External S3 bucket path For Ingestion Incremental Data';

-- COMMAND ----------

SHOW CATALOGS;

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS formula1_incr
  MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/'
  COMMENT 'THIS IS THE MAIN CATALOG FOR FORMULA1 PROJECT'

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS formula1_incr.landing;
CREATE SCHEMA IF NOT EXISTS formula1_incr.bronze
    MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/bronze';
CREATE SCHEMA IF NOT EXISTS formula1_incr.silver
    MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/silver';
CREATE SCHEMA IF NOT EXISTS formula1_incr.gold
    MANAGED LOCATION 's3://databrickks-demo-ingestion-formula1/gold';         

-- COMMAND ----------

SELECT current_catalog();

-- COMMAND ----------

USE CATALOG formula1_incr;

-- COMMAND ----------

SHOW SCHEMAS;

-- COMMAND ----------

CREATE EXTERNAL VOLUME formula1_incr.landing.files
LOCATION 's3://databrickks-demo-ingestion-formula1/landing';

-- COMMAND ----------

-- MAGIC %fs ls /Volumes/formula1_incr/landing/files