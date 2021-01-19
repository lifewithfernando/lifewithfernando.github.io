from typing import Any

import airflow

from airflow import models
from airflow.operators import bash_operator

gcs_to_bq = None # type: Any
try:
    from airflow.contrib.operators import gcs_to_bq
except ImportError:
    pass

if gcs_to_bq is not None:
    args = {
        'owner': 'Airflow',
        'start_date': airflow.utils.dates.days_ago(2)
    }

    dag = models.DAG(
        dag_id='gcs_to_bq_operator', default_args=args,
        schedule_interval=None)
    
    create_test_dataset = bash_operator.BashOperator(
        task_id='create_airflow_test_dataset',
        bash_command='bq mk airflow_test',
        dag=dag
    )

    # [START howto_operator_gcs_to_bq]
    load_csv = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
        task_id='gcs_to_bq',
        bucket='fernando-gcs',
#        source_objects=['jsonfiles/ndjson7.csv'],
        source_format = 'NEWLINE_DELIMITED_JSON',
        source_objects=['jsonfiles/ndjson5.json'],
        destination_project_dataset_table='airflow_test.gcs_to_bq_table',
        bash_command='bq load --autodetect --source_format=NEWLINE_DELIMITED_JSON airflow_test.gcs_to_bq_table gs://fernando-gcs/jsonfiles/ndjson5.json',
        write_disposition='WRITE_TRUNCATE',
        autodetect = True,
        dag=dag
    )
    # [END howto_operator_gcs_to_bq]

    delete_test_dataset = bash_operator.BashOperator(
        task_id='delete_airflow_test_dataset',
        bash_command='bq rm -r airflow_test',
        dag=dag)
    
    create_test_dataset >> load_csv >> delete_test_dataset

