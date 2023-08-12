import time
import random

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def counter_task():
    for i in range(random.randint(10,30)):
        time.sleep(1)
        logger.info(f"Counting - {i+1}")
