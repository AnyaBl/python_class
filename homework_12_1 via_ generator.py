import time
import functools
import datetime


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        starting_time = time.time()
        val = func(*args, **kwargs)
        ending_time = time.time()
        run_time = ending_time - starting_time
        print(f"Функцію {func.__name__} завершено через {run_time:.10f} секунд.")
        return val

    return wrapper


@timer
def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


f = fib(101)
print(list(f))
