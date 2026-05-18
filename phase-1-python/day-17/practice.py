from contextlib import contextmanager
from functools import wraps
def my_logger(func):
    import logging
    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return func(*args, **kwargs)

    return wrapper
@my_logger
def read_file(filename, mode):
    with open(filename, mode) as f:
        return f.read()

content = read_file('practice.txt', 'r')
print(content)
