# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE VIEW formula1.gold.v_constructor_standing
# MAGIC AS
# MAGIC WITH constructor_session_summary
# MAGIC AS
# MAGIC   (SELECT r.season,
# MAGIC         c.constructor_id,
# MAGIC         c.constructor_name,
# MAGIC         c.nationality,
# MAGIC         COUNT(*) AS race_starts,
# MAGIC         SUM(r.points) AS total_points,
# MAGIC         COUNT_IF(r.is_win) AS number_of_wins,
# MAGIC         COUNT_IF(r.is_podium) AS number_of_podiums
# MAGIC     FROM formula1.gold.fact_session_results r
# MAGIC     JOIN formula1.gold.dim_constructors c
# MAGIC       ON r.constructor_id = c.constructor_id 
# MAGIC   GROUP BY r.season,
# MAGIC         c.constructor_id,
# MAGIC         c.constructor_name,
# MAGIC         c.nationality)    
# MAGIC SELECT season,
# MAGIC        constructor_id,
# MAGIC        constructor_name,
# MAGIC        nationality,
# MAGIC        RANK() OVER (PARTITION BY season ORDER BY total_points DESC, number_of_wins DESC) AS standing,
# MAGIC        race_starts,
# MAGIC        total_points,
# MAGIC        number_of_wins,
# MAGIC        number_of_podiums
# MAGIC   FROM constructor_session_summary;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM formula1.gold.v_constructor_standing WHERE season = 2025