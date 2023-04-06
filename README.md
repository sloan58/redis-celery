# Python Celery with Redis

This is a small demo application that uses Python Celery with Redis

> pip install -r requirements.txt

> Install Redis using docker or apt-get/dnf install -y redis 

### tasks.py
```python
from celery import Celery

# Init Celery app
# Built using Python 3.9.6
app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')


# Define async job call_api
@app.task
def call_api(data):
    return data
```

In one terminal, run this Celery worker using `celery -A tasks worker --loglevel=INFO`

In another terminal, run the backend ui, use `celery -A tasks flower --port=5555`

The "backend" web interface will be served at http://localhost:5555

### main.py

```python
from tasks import call_api
from time import sleep


# Simulate some long-running process
# that builds a large result list
def some_long_running_task():
    sleep(5)
    res = []
    for i in range(1, 100):
        res.append(i)
    return res


if __name__ == '__main__':
    # Call long-running process to collect results
    results = some_long_running_task()

    # Push new queued job to Celery
    # for each result from long-running job
    # use .delay to push to async queue
    for result in results:
        call_api.delay(result)

```

The main.py file runs a simulated application that performs some long-running task
and then hands the results off to run as async tasks in Celery.

> Call `.delay()` to run the Celery tasks async (otherwise they will run sync)