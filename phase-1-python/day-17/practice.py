from contextlib import contextmanager

@contextmanager
def simple_file_manager(filename, mode):
    print("Log: Opening...")
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()
        print("Log: Closed!")

# Usage
with simple_file_manager('practice.txt', 'r') as f:
    print(f.read())