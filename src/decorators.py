from typing import Any, Callable
import time
from src.masks import get_mask_account
from functools import wraps

def log(filename: str | Any = None) -> Any:
    def logging_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # time_1 = time()
                result = func(*args, **kwargs)
                # time_2 = time()
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f'{func.__name__} is ok\n')
                else:
                    print(f'{func.__name__} is ok\n')
                return result
            except Exception as error_:
                if filename is not None:
                    with open(filename, 'a') as file:
                        file.write(f'{func.__name__} error: {error_}, input: {args}, {kwargs}\n')
                else:
                    print(f'{func.__name__} error: {error_}, input: {args}, {kwargs}\n')
                # raise error_
            except ZeroDivisionError as error_2:
                if filename is not None:
                    with open(filename, 'a') as file:
                        file.write(f'{func.__name__} error: {error_2}, input: {args}, {kwargs}\n')
                else:
                    print(f'{func.__name__} error: {error_2}, input: {args}, {kwargs}\n')
                # raise error_2
        return wrapper
    return logging_decorator

@log(filename = 'log.txt')
def my_function(x, y):
    return x / y

my_function(2, 0)

