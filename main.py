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
