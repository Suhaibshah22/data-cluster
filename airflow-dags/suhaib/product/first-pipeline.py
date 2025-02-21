"""
Auto-generated Airflow DAG
Do not modify this file directly,
update the pipeline configuration file.

Pipeline Name: pg_to_snowflake_ingest
Description: Extract some data and load some data
"""

import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1
}

dag = DAG(
    dag_id="pg_to_snowflake_ingest",
    default_args=default_args,
    description="Extract some data and load some data",
    schedule_interval="0 4 * * *",
    catchup=False
)

def extract_and_load(**context):
    """
    Placeholder Python function that simulates:
      - Extracting data from Postgres
      - Loading it into Snowflake
    """
    print("Extracting from Postgres: host=subscription-db.exampled.com, db=subscriptions, table=")
    print("Loading data into Snowflake table: analytics.user_subscriptions")
    print("Success: Data transferred from Postgres to Snowflake!")

extract_and_load_task = PythonOperator(
    task_id="extract-and-load",
    python_callable=extract_and_load,
    dag=dag
)
