import cProfile
import pstats
import time
'''
def download_data():
    time.sleep(1)
def compute_metrics():
    result=sum(x**2 for x in range(200000))
    return result
def run_pipeline():
    download_data()
    compute_metrics()

if __name__=="__main__":
    profiler=cProfile.Profile()

    profiler.enable()
    run_pipeline()
    profiler.disable()

    stats=pstats.Stats(profiler).sort_stats("cumulative")
    stats.print_stats(10)'''

import cProfile
from concurrent.futures import ThreadPoolExecutor
import time

def process_chunk(x):
    time.sleep(0.5)
    return x * x

if __name__ == "__main__":
    profiler = cProfile.Profile()
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        profiler.enable()
        results = list(executor.map(process_chunk, [10, 20, 30]))
        profiler.disable()
        
    profiler.print_stats()