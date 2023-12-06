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


@measure_time
def my_function_sum():
    suma = 0
    for i in range(15000000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_function_np():
    total = np.sum(np.arange(15000000), dtype=np.int64)
    print("Sum is:", total)


my_function()
# Czas wykonania funkcji my_function: 0.9335784912109375 sekundy
# 11:20
my_function_np()

# Sum is: 112499992500000
# Czas wykonania funkcji my_function: 0.5210573673248291 sekundy
# Sum is: 112499992500000
# Czas wykonania funkcji my_function_np: 0.044116973876953125 sekundy
my_function_sum()

# Sum is: 112499992500000
# Czas wykonania funkcji my_function: 0.532174825668335 sekundy
# Sum is: 112499992500000
# Czas wykonania funkcji my_function_np: 0.0420536994934082 sekundy
# Sum is: 112499992500000
# Czas wykonania funkcji my_function_sum: 0.6128120422363281 sekundy