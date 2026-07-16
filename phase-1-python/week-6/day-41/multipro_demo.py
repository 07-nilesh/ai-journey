import multiprocessing
import os 
import time

def compute_square(number):
    pid=os.getpid()
    print(f"[worker pid {pid} computing square for {number}]")
    return number*number

if __name__=="__main__":
    number_list=[1,2,3,4]

    print("low level approach A")
    worker_process=multiprocessing.Process(target=compute_square,args=(10,))
    worker_process.start()
    worker_process.join()

    print(f"\n high level approch")
    with multiprocessing.Pool (processes=4) as pool:
        results=pool.map(compute_square,number_list) 
    print(f"\n final results from pool :{results}")