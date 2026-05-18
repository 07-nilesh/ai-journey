from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    @wraps(orig_func)  # This decorator helps to preserve the original function's metadata
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper
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
@my_logger # The order of decorators matters. The my_logger will be applied first, and then my_timer will wrap the result of that.
def display_info(name, age):
    print('Display_info ran with arguments ({}, {})'.format(name,age))

display_info('Nilesh', 22)
display_info('Arya', 28)