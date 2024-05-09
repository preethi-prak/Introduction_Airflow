from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class MyCustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, my_param, *args, **kwargs):
        super(MyCustomOperator, self).__init__(*args, **kwargs)
        self.my_param = my_param

    def execute(self, context):
        self.log.info(f"Hello from MyCustomOperator with param: {self.my_param}")
