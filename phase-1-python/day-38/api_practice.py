import requests
import pandas as pd
import datetime
import time
import csv
get_url = "https://blockchain.info/ticker"

print("Starting Bitcoin Tracker... Press Ctrl+C to Stop.")

while True:
    response = requests.get(get_url)
    data = response.json()
    btc_price = data['USD']['last']
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    single_row = pd.DataFrame({'Timestamp': [timestamp], 'Price': [btc_price]})
    print(f"{timestamp} - Bitcoin Price: ${btc_price}")
    with open('bitcoin_prices.csv', 'a') as f:
        writer = csv.writer(f)
        if f.tell() == 0:  # If file is new, write the header
            writer.writerow(['Timestamp', 'Price'])
        writer.writerow([timestamp, btc_price])
    print(f"{timestamp} - Bitcoin Price: ${btc_price}")
    time.sleep(60)  # Wait for 60 seconds before the next update