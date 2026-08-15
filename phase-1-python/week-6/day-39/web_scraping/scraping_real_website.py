from bs4 import BeautifulSoup
import requests
import pandas as pd

url=('http://books.toscrape.com/catalogue/category/books/poetry_23/index.html')
res = requests.get(url)
soup=BeautifulSoup(res.text,'lxml')
books=soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
data_list=[]
print("Scraping started...")
for book in books:
    title=book.find("h3").text
    rating=book.find("p",class_="star-rating")['class'][1]
    price=book.find("p",class_="price_color").text
    
    data_list.append({"title":title,
          "price":price,
          "rating":rating})
df=pd.DataFrame(data_list)
df.to_csv("books_info.csv",index=False)
print("scraping finished...")



