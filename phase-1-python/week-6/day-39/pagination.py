import requests
import time

current_page=1
has_more_data=True
all_servers_logs=[]
back_off_dealy=2
while True:
    url=f"https://api.mockdata.com/sensor-logs?page={current_page}"
    res=requests.get(url)    
    if res.status_code==200:
        data=res.json()
        all_servers_logs.extend(data["logs"])
        if data["has_more"]==True:
            current_page+=1
        else:
            break
    if res.status_code==429:

        time.sleep(back_off_dealy)
        back_off_dealy*=2
        continue


