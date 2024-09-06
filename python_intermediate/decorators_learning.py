import time
import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(2, 3))


def enlarge_first_param_5x(func):
    def wrapper(*args, **kwargs):
        modified_args = list(args)
        if modified_args:
            modified_args[0] = modified_args[0] * 5
        modified_args = tuple(modified_args)
        result = func(*modified_args, **kwargs)
        return result
    return wrapper

@enlarge_first_param_5x
def get_5x(num):
    return num

print(get_5x(5))
        


#==============================================================

def log_time(func):
    def wrapper(*args, **kwargs):
        stime = time.time()
        result = func(*args, **kwargs)
        print(f"Total time taken for execution = {time.time() - stime:.6f}")
        return result
    return wrapper


@log_time
def count_to(x):
    for i in range(x):
        pass

count_to(1000)

#==============================================================

def my_decorator(func):
    def wrapper():
        print(f"Starting function execution {func.__name__}")
        func()
        print(f"Ending function execution {func.__name__}")
    return wrapper


@my_decorator
def say_hello():
    print("Hello Decorators.")


say_hello()


        
