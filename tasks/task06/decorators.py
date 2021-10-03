import time


def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")

    return wrapper
