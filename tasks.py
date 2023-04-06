from celery import Celery

# Init Celery app
# Built using Python 3.9.6
app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')


# Define async job call_api
@app.task
def call_api(data):
    return data


