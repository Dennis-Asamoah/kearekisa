from celery.decorators import task
from celery.utils.log import logger
import time 

print(45550000000000)
@task(name='long_task')
def long_task(val):
    print(4555)
    time.sleep(1)
    print(12345)
    return val
