import logging
import time

LOG = logging.getLogger()
logging.basicConfig()
LOG.setLevel(logging.INFO)


class DelayDecorator(object):
    def __int__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        time.sleep(kwargs.get("delay", 10))
        start_time = time.time()
        LOG.info(f"{self.func.__name__} started at {start_time}")
        result = self.func(*args, **kwargs)
        end_time = time.time()
        LOG.info(f"{self.func.__name__} started at {end_time} and \
        total time taken to execute: {end_time-start_time}")
        return result
