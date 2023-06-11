import logging
import time

LOG = logging.getLogger(__name__)
logging.basicConfig()
LOG.setLevel(logging.INFO)


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        LOG.info(f"{func.__name__} started at {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        LOG.info(f"{func.__name__} started at {end_time} and \
        total time taken to execute: {end_time-start_time}")
        return result
    return wrapper


@time_logger
def mul(a, b):
    return a*b


@time_logger
def add(a, b):
    return a+b


@time_logger
def sub(a, b):
    return a-b


@time_logger
def div(a, b):
    return a//b


for a, b in [(2, 3), (9, 1), (10, 89)]:
    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))


