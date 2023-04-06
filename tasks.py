from celery import Celery
from time import sleep
import random

# Init Celery app
# Built using Python 3.9.6
app = Celery('my_app_tasks', broker='redis://localhost', backend='redis://localhost')


# Define async job call_api
@app.task
def call_api(data):
    # Perform some operation on the input data
    result = data * 2

    # Simulate network delay calling API
    sleep(random.uniform(0, 1))

    return result


