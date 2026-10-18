# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d31836cb-3fc2-4e0d-a1d1-2b593a0306f0",
# META       "default_lakehouse_name": "LH_config",
# META       "default_lakehouse_workspace_id": "d059eaaf-2e86-42c7-8e7a-ddd593ae6b60",
# META       "known_lakehouses": [
# META         {
# META           "id": "d31836cb-3fc2-4e0d-a1d1-2b593a0306f0"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE ingestion_run_plan
# MAGIC USING DELTA
# MAGIC AS
# MAGIC SELECT
# MAGIC     t.*,
# MAGIC     s.source_type,
# MAGIC     s.fabric_connection_name,
# MAGIC     s.host,
# MAGIC     s.port,
# MAGIC     s.database_name
# MAGIC FROM list_of_table t
# MAGIC INNER JOIN metadata_mysql s
# MAGIC     ON t.source_id = s.source_id
# MAGIC WHERE t.is_active = 1
# MAGIC   AND s.is_active = 1;


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
