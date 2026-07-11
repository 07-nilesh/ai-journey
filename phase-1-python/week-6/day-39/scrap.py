import requests
from bs4 import BeautifulSoup
import pandas as pd

url="http://books.toscrape.com/catalogue/page-1.html"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
scrapped_data=[]
book_conatiner=soup.select('article.product_pod')
for book in book_conatiner:
    title=book.h3.a.text
    price=book.select_one('p.price_color').text
    rating_class=book.select_one('p.star-rating')['class']
    rating=rating_class[1]

    scrapped_data.append({
        "Title":title,"Price":price,"Rating":rating
    }) 
books_dataframe=pd.DataFrame(scrapped_data)
books_dataframe.to_csv('extract_books.csv',index=False)
print(books_dataframe.head(3))
