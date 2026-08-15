from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

driver= webdriver.Chrome()
driver.get("http://books.toscrape.com/")
# name= driver.title
# print(name)
# url=driver.current_url
# print(url)
# driver.close()

# driver.implicitly_wait(20)
# # Add a cookie (just for demo)
# driver.add_cookie({"name": "test_cookie", "value": "12345"})
# print("Cookies before delete:", driver.get_cookies())
# # Delete all cookies
# driver.delete_all_cookies()
# print("Cookies after delete:", driver.get_cookies())
# driver.quit()

#/To set the size of the window
driver.set_window_size(1024,768)
size=driver.get_window_size()
print("window size :",size)

#To set the position of the window
driver.set_window_position(0,0)
pos=driver.get_window_position()
print("window : ",pos)

#/To maximize the window
driver.maximize_window()
size=driver.get_window_size()
print(size)

time.sleep(30)
driver.quit()
