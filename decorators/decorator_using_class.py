import logging
import time

LOG = logging.getLogger()
logging.basicConfig()
LOG.setLevel(logging.INFO)


class DelayDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        LOG.info("Sleeping for {} secs".format(kwargs.get("delay", 10)))
        time.sleep(kwargs.get("delay", 10))
        start_time = time.time()
        LOG.info(f"{self.func.__name__} started at {start_time}")
        result = self.func(*args, **kwargs)
        end_time = time.time()
        LOG.info(f"{self.func.__name__} ended at {end_time} and \
        total time taken to execute: {end_time-start_time}")
        return result



@DelayDecorator
def add(a, b):
    return a+b

LOG.info(add(2, 6))
