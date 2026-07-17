import os
import time 
from concurrent.futures import ProcessPoolExecutor

def parse_csv_mock(file_name):
    calc=sum(x**2 for x in range(10000))
    
    time.sleep(0.1)
    return {"file_name": file_name, "processed_records": 5000, "status": "SUCCESS", "worker_pid": os.getpid()}

if __name__=="__main__":
    mock_files=[f"file_{i}.csv" for i in range(100)]
    start_time=time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:
        results=executor.map(parse_csv_mock,mock_files)
        for result in results:
            print(result)
    end_time=time.time()
    print(f"\nTotal parallel execution duration: {end_time - start_time:.4f} seconds")

import os
from concurrent.futures import ProcessPoolExecutor

def calculate_cubes(x):
    return x ** 3

if __name__ == "__main__":
    payload = [1, 2, 3]
    with ProcessPoolExecutor(max_workers=2) as executor:
        map_generator = executor.map(calculate_cubes, payload)
        
    # NOTICE: The generator is read OUTSIDE the context manager block
    for result in map_generator:
        print(result)
