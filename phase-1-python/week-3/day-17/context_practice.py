from contextlib import contextmanager

@contextmanager
def log_file_operation(filename, mode):
    print(f"--- Opening file: {filename} ---")
    # Step 1: Open the resource
    f = open(filename, mode)
    try:
        # Step 2: Yield the resource to the 'as' variable
        yield f 
    finally:
        # Step 3: Ensure it closes no matter what happens in the block
        f.close()
        print(f"--- Closing file: {filename} ---")

# Usage: This handles opening, reading, and closing with logs!
with log_file_operation('practice.txt', 'r') as f:
    content = f.read()
    print(f"File Content: {content}")