import time
import numpy as np


# pip install numpy

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sekundy")
        return result

    return wrapper


@measure_time
def my_function():
    # pass
    total = sum(range(15000000))
    print("Sum is:", total)

# def my_function_np():


# my_function()
# Czas wykonania funkcji my_function: 0.9335784912109375 sekundy
# 11:20
