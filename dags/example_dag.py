from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('Introduction_Airflow',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    start >> end
