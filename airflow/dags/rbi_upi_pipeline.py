from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="rbi_upi_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["rbi", "upi", "etl"],
) as dag:

    extract_upi = BashOperator(
        task_id="extract_upi",
        bash_command="python /opt/airflow/etl/extract_all_upi.py",
        cwd="/opt/airflow",
    )

    load_mysql = BashOperator(
        task_id="load_mysql",
        bash_command="python /opt/airflow/etl/load_mysql.py",
        cwd="/opt/airflow",
    )
    
    validate_data = BashOperator(
    task_id="validate_data",
    bash_command="python /opt/airflow/etl/validate_monthly_upi.py",
    cwd="/opt/airflow",
    )

    extract_upi >> validate_data >> load_mysql