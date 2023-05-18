#######################################################

# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.
def start_end_decorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
    
print_name()

print()

# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name)
print_name()

#######################################################

@start_end_decorator
def print_name():
    print('Alex')
    
print_name()

#######################################################

def start_end_decorator_2(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')
    return wrapper

@start_end_decorator_2
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

#######################################################

def start_end_decorator_3(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_3
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

#######################################################

print(add_5.__name__)
help(add_5)

#######################################################

import functools
def start_end_decorator_4(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_4
def add_5(x):
    return x + 5
result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)

#######################################################

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

#######################################################

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")
    
greet('Alex')

#######################################################

# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator_4
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')

#######################################################

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print("Hello!")
    
say_hello(5)
say_hello(5)

#######################################################

# Some typical use cases
# Use a timer decorator to calculate the execution time of a function
# Use a debug decorator to print out some more information about the called function and its arguments
# Use a check decorator to check if the arguments fulfill some requirements and adapt the bevaviour accordingly
# Register functions (plugins)
# Slow down code with `time.sleep()` to check network behaviour
# Cache the return values for memoization (https://en.wikipedia.org/wiki/Memoization)
# Add information or update a state