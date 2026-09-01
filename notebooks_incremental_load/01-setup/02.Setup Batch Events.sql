-- Databricks notebook source
CREATE SCHEMA IF NOT EXISTS formula1.control
    MANAGED LOCATION 'abfss://formula1@databrickscourseextdl1.dfs.core.windows.net/control';

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS formula1.control.batch_events
(
    batch_id INT,
    event_timestamp TIMESTAMP
)

-- COMMAND ----------

INSERT INTO formula1.control.batch_events
VALUES (1, current_timestamp());

-- COMMAND ----------

INSERT INTO formula1.control.batch_events
VALUES (2, current_timestamp());

-- COMMAND ----------

SELECT * FROM formula1.control.batch_events;