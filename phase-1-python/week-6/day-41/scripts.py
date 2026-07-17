from memory_profiler import profile  # not mandatory 
import time
import numpy as np
import gc

global_tracker=[]
@profile
def simulate_stream_buffer():
    print("intialising")
    heavy_matrix_buffer=(float(i) for i in range(1000000)) # generator mirage increment to 0 after that
    time.sleep(0.2)
    secondary=np.array(heavy_matrix_buffer)
    time.sleep(0.5)
    global_tracker.append(heavy_matrix_buffer)
    del heavy_matrix_buffer
    gc.collect()
    print("primary heavy buffer deleted")
    shape=np.shape(secondary)

    return shape

if __name__=="__main__":
    simulate_stream_buffer()

# Run : python -m memory_profiler script.py