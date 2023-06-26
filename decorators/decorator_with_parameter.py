import time

import requests
import time

def execute_n_times(n, wait_time):
    def decorator_func(func):
        results = list()

        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
                results.append(result)
                time.sleep(wait_time)
            return results
        return wrapper
    return decorator_func