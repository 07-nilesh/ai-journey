import time
import pandas as pd
import urllib.robotparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
try:
    gatekeeper = urllib.robotparser.RobotFileParser()
    gatekeeper.set_url("https://news.ycombinator.com/robots.txt")
    gatekeeper.read()
    target_url = "https://news.ycombinator.com/"
    if gatekeeper.can_fetch("*", target_url):
        print(f"Allowed to scrape: {target_url}")
except Exception as e:
    print(f"An error occurred while checking robots.txt: {e}")

chrome_options = Options()
chrome_options.add_argument("--headless")
automated_browser = webdriver.Chrome(options=chrome_options)
try:
    target_url = "https://news.ycombinator.com/"
    automated_browser.get(target_url)
    time.sleep(3)
    
    #top 10 hacker news
    main_heading_element = automated_browser.find_elements(By.CLASS_NAME, "titleline")
    data=[]
    for i in range(10):
        data.append(main_heading_element[i].text)
        print(f"Title {i+1}: {main_heading_element[i].text}")
    df = pd.DataFrame(data, columns=["Title"])
    df.to_csv("hacker_news_top10.csv", index=False, encoding="utf-8")
    
        
except Exception as e:
    print(f"An error occurred while scraping the website: {e}")
finally:
    automated_browser.quit()
    print("Automated browser closed successfully.")