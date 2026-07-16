import time
from concurrent.futures import ThreadPoolExecutor
'''
def handle_frame(id):
    if id == 2:
        raise RuntimeError("VLM processing timeout crash!")
    return f"Processed_{id}"

with ThreadPoolExecutor(max_workers=2) as executor:
    task = executor.submit(handle_frame, 2)
    time.sleep(0.5)
    print(f"Task status: {task.done()}")

print("Pipeline execution checklist verified.")

'''

from concurrent.futures import ProcessPoolExecutor

class LocalFrameProcessor:
    def __init__(self, factor):
        self.factor = factor
        
    def process_matrix(self, frame_id):
        return f"Frame_{frame_id}_Scaled_By_{self.factor}"

if __name__ == "__main__":
    processor = LocalFrameProcessor(factor=2)
    payloads = [1, 2, 3, 4]
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        # Bug location is within the map call below
        results = executor.map(processor.process_matrix, payloads)
        
    print(list(results))