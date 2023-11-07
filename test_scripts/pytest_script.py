# Databricks notebook source
start_year = 2023
end_year = 2027


year_months = []

for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        year_month = year * 100 + month
        year_months.append(year_month)

import pandas

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_database()

# COMMAND ----------


