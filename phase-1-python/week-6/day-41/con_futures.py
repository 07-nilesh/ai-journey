from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os
import time
'''
def download_frame_log(frame_id):
    print(f"[Worker] Starting download for Frame {frame_id} on PID {os.getpid()}")
    time.sleep(1)
    return f"frame_{frame_id}_saved.bin"
if __name__=="__main__":
    frame_batch=[101,102,103,104]

    print("--- 1. Executing via ThreadPoolExecutor (I/O Strategy) ---")
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results=executor.map(download_frame_log,frame_batch)
    print(f"Thread Execution Complete. Results: {list(thread_results)}\n")
    print("--- 2. Executing via ProcessPoolExecutor (CPU/Isolated Strategy) ---")
    with ProcessPoolExecutor(max_workers=4) as executor:
        process_results=executor.map(download_frame_log,frame_batch)
    print(f"Process Execution Complete. Results: {list(process_results)}")
    '''
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def heavy_math_crunch(n):
    # Pure CPU-bound arithmetic loop
    count = 0
    for i in range(n):
        count += (i ** 2)
    return count

if __name__ == "__main__":
    # A heavy payload array to crunch 4 times
    crunch_payload = [10_000_000, 10_000_000, 10_000_000, 10_000_000]
    
    # Execution Variant A: ThreadPoolExecutor
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(heavy_math_crunch, crunch_payload))
    print(f"ThreadPool Duration: {time.time() - start_time:.4f} seconds")
    
    # Execution Variant B: ProcessPoolExecutor
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(heavy_math_crunch, crunch_payload))
    print(f"ProcessPool Duration: {time.time() - start_time:.4f} seconds")