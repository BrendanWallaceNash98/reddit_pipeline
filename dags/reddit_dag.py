from airflow import DAG
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Brendan Wallace Nash',
    'start_date': datetime(2023, 1, 1),

}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='elt_reddit_pipeline',
    dafault_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'elt', 'pipeline']
)