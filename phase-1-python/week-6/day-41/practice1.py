from concurrent.futures import ProcessPoolExecutor
import os

def process_crowd_file(file_id):
    print(f"process id :{os.getpid()}")
    calculation_result=sum(x**2 for x in range(5000000))
    return (file_id,calculation_result)
if __name__=="__main__":
    mock_ids=list(range(100))
    with ProcessPoolExecutor(max_workers=4) as executor:
        result=executor.map(process_crowd_file,mock_ids)
    print(f"results:{list(result)}")