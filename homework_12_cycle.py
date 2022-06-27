import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Функцію {func.__name__} завершено через {run_time:.10f} секунд.")
        return val

    return wrapper



@timer
def fibonnacci(n):
    First = 0
    Second = 1
    Sum = 0

    for Num in range(0, n):
        print(First, end = '  ')
        Sum = Sum + First
        Next = First + Second
        First = Second
        Second = Next
    print("\nThe Sum of Fibonacci Series Numbers = %d" %Sum)

fibonnacci(100)
