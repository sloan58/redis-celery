from celery import Celery

# Init Celery app
# Run this app using `celery -A tasks worker --loglevel=INFO`
# To run the backend ui, use `celery -A tasks flower --port=5555`
# The web interface will be served at http://localhost:5555
# Built using Python 3.9.6
app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')


# Define async job call_api
@app.task
def call_api(data):
    return data


