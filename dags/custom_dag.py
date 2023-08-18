import datetime

import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="custom_dag",
    schedule=datetime.timedelta(hours=4),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    task1 = EmptyOperator(task_id="task1")
    task2 = EmptyOperator(task_id="task2")
    task3 = EmptyOperator(task_id="task3")

    task1 >> task2 >> task3