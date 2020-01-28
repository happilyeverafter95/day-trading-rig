from airflow import DAG
from airflow.operators import PythonOperator, ShortCircuitOperator,\
    EmailOperator
from airflow.utils.trigger_rule import TriggerRule

from datetime import datetime

from listener.listener import Listener
from listener.email import EmailService

listener = Listener()
email_service = EmailService()

default_args = {
    'owner': 'M & E',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'email': ['yymgu@edu.uwaterloo.ca'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
}

with DAG(
    'PriceAlerter',
    default_args=default_args,
    schedule_interval='*/5 9-17 * * *',
    catchup=False,
) as dag:
    price_listener = PythonOperator(
        task_id='listener',
        python_callable=listener.listen,
    )
    email_trigger = ShortCircuitOperator(
        task_id='email_trigger',
        python_callable=lambda: True if listener.trigger else False,
        trigger_rule=TriggerRule.NONE_FAILED,
    )
    email = EmailOperator(
        task_id='email',
        to=email_service.email_list,
        subject=email_service.get_email_subject(listener.summary),
        html_content=email_service.get_html_content(listener.summary),
    )

price_listener.set_downstream(email_trigger)
email_trigger.set_downstream(email)
