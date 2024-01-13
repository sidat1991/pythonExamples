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


@execute_n_times(3, 5)
def check_get_api_status_code(url):
    res = requests.get(url, verify=False)
    return res.status_code
