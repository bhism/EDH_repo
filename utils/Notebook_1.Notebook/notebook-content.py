# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "9c102c71-e18c-4d99-b0aa-172bead53e27",
# META       "default_lakehouse_name": "LH_config",
# META       "default_lakehouse_workspace_id": "d059eaaf-2e86-42c7-8e7a-ddd593ae6b60",
# META       "known_lakehouses": [
# META         {
# META           "id": "9c102c71-e18c-4d99-b0aa-172bead53e27"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "b43f4d7f-0d64-4d5d-a68a-6d6fc0cf9fb3",
# META       "known_warehouses": [
# META         {
# META           "id": "b43f4d7f-0d64-4d5d-a68a-6d6fc0cf9fb3",
# META           "type": "Lakewarehouse"
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
