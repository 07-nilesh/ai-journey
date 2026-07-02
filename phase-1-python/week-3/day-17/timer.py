from functools import wraps
def my_timer(orig_func):
    import time
    @wraps(orig_func)  # This decorator helps to preserve the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = orig_func(*args, **kwargs)
        end_time = time.time()-start_time
        print('Function {} took {} seconds to execute.'.format(orig_func.__name__, end_time))
        return result

    return wrapper
import time
@my_timer
def display_info(name, age):
    time.sleep(1)  # Simulating a time-consuming function by adding a sleep delay
    print('Display_info ran with arguments ({}, {})'.format(name, age))
display_info('Nilesh', 22)
display_info('Arya', 28)
print(display_info.__name__)  # This will print the name of the original function, which is 'display_info', demonstrating that the wrapper function retains the original function's metadata.
