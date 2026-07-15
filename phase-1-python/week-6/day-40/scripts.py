from pathlib import Path
import pandas as pd
import csv

dataframe_accumulator=[]
target=Path.cwd()/"campus_logs"
if target.exists():
    for file in target.iterdir():
        if file.is_file() and file.suffix == ".csv":
            df_chunk=pd.read_csv(file)
            dataframe_accumulator.append(df_chunk)
    if dataframe_accumulator:
        master=pd.concat(dataframe_accumulator,ignore_index=True)
        master.to_csv("master_data.csv",index=False)
        master.info()
    
    
