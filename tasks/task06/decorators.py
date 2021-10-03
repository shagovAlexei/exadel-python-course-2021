import time
from datetime import datetime

def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f"{func.__name__} call  {datetime.now() - start} seconds")
        return result
    return wrapper


@measure_elapsed_time
def my_fn1(arg1, arg2):
    time.sleep(0.5)
    return arg1 + arg2

@measure_elapsed_time
def test_func2(name: str, status: bool):
    time.sleep(0.8)
    print("My name is {}, and my status is {}".format(name, status))


print("my_fn1 result:", my_fn1(1, 2))