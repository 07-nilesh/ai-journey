import os
import sys
from datetime import datetime

project_dir="/home/nilesh/worspace/automation_project"

log_file_path=os.path.join(project_dir,"daily_execution.log")
data_input_path=os.path.join(project_dir,"raw_data.csv")

def daily_run_pipeline():
    try:
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not os.path.exists(data_input_path):
            raise FileNotFoundError(f"missing abs data: {data_input_path}")
        
        with open(log_file_path,"a") as log_file:
            log_file.write(f"[{current_time}] SUCCESS :pipeline executed.")
    except Exception as error_msg:
        with open(log_file_path,"a") as log_file:
            log_file.write(f"[{datetime.now()}] CRITICAL ERROR : {str(error_msg)}")
        sys.exit(1)
if __name__=="__main__":
    daily_run_pipeline()
