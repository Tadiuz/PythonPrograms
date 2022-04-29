import datetime as dt

from datetime import timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator

from airflow.operators.python import PythonOperator

import pandas as pd

def CSVToJson():

    df =  pd.read_csv('csv_library.csv')

    for i,r in df.iterrows():

        print(r['Names'])

    df.to_json('fromAirflow.JSON',orient='records')


default_args = {

    'owner': 'rodrigo',

    'start_date': dt.datetime(2022, 2, 16),

    'retries': 1,

    'retry_delay': dt.timedelta(minutes=1),

}


with DAG('MyCSVDAG_v2',

         default_args=default_args,

         schedule_interval=timedelta(minutes=1),      

         # '0 * * * *',

         ) as dag:

    print_starting = BashOperator(task_id='starting',bash_command='echo "I am reading the CSV now....."')

    CSVJson = PythonOperator(task_id='convertCSVtoJson', python_callable=CSVToJson)

    print_starting >>  CSVJson