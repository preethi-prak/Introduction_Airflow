from airflow import DAG
from airflow.operators.empty import EmptyOperator  # Updated import statement
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('Introduction_Airflow',
         default_args=default_args,
         schedule='@daily',  # Updated parameter
         catchup=False) as dag:

    start = EmptyOperator(task_id='start')  # Updated class name
    end = EmptyOperator(task_id='end')  # Updated class name

    start >> end
