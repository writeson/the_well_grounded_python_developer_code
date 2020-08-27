
import functools
from random import uniform
from time import sleep, time


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(delay):
        start_time = time()
        print("starting timing")
        result = func(delay)
        print(f"task elapsed time: {time() - start_time}")
        return result
    return wrapper


@timing_decorator
def complex_task(delay):
    sleep(delay)
    return "task done"


def main():
    for _ in range(3):
        delay = uniform(0.25, 3)
        print(complex_task(delay))


if __name__ == "__main__":
    main()
