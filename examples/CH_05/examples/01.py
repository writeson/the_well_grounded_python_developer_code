
import functools
from random import uniform
from time import sleep, time


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time()
        print("starting timing")
        result = func()
        print(f"task elapsed time: {time() - start_time}")
        return result
    return wrapper


@timing_decorator
def complex_task():
    delay = uniform(0.25, 3)
    sleep(delay)
    return "task done"


def main():
    print("running")
    for _ in range(5):
        print(complex_task())
