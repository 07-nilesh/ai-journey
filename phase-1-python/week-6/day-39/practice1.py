import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#The server reads it as a normal human visitor
custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
url="https://news.ycombinator.com/"
response=requests.get(url,headers=custom_headers)

soup=BeautifulSoup(response.text,"html.parser")
stories_data=[]
story_row=soup.select("tr.athing") #the parent table row container for every single post

for row in story_row:
    title_span=row.select_one("span.titleline")
    if title_span:
        title_text=title_span.a.text
        story_url=title_span.a["href"]

        subtext_row=row.find_next_sibling("tr")
        score_span=subtext_row.select_one("span.score")
        score_text=score_span.text if score_span else "0 points"
        stories_data.append({
            "Headline":title_text,"URL":story_url,"Score": score_text
        })
dataframe=pd.DataFrame(stories_data).head(10)
print(dataframe)