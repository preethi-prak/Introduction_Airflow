from airflow import DAG
from airflow.utils.dates import days_ago
from my_custom_operator import MyCustomOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'my_custom_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
    start_date=days_ago(2),
    tags=['example'],
) as dag:
    custom_task = MyCustomOperator(
        task_id='print_hello',
        my_param='World'
    )

custom_task
