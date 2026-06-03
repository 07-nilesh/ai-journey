import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

book_title = soup.find('h1').text
book_price = float(soup.find('p', class_='price_color').text.strip('Â£'))  # Remove the pound symbol and convert to float
print(f"Book Title: {book_title}")
print(f"Book Price: {book_price}")
product_description = soup.find('div', id='product_description').find_next_sibling('p').text
print(f"Product Description: {product_description}")
book_rating = soup.find('p', class_='star-rating')['class'][1]  # Get the second class which indicates the rating
print(f"Book Rating: {book_rating}")

data = {
    'Title': [book_title],
    'Price': [book_price],
    'Description': [product_description],
    'Rating': [book_rating]
}
df = pd.DataFrame(data)
# This replaces your entire 'with open()' block perfectly!
df.to_csv("book_data.csv", index=False, encoding="utf-8")
# Step 4: Print the DataFrame to confirm it looks like a clean table
print("--- Scraped Data Saved to CSV successfully! View below: ---")
print(df)
import bs4
mock_html = "<div><p class='main'>Hello Indore!</p></div>"
soup = bs4.BeautifulSoup(mock_html, 'html.parser')
print(soup.find('p', class_='main').text)

