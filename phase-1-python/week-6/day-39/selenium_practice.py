from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Step 1: Initialize the browser options container configuration layout
chrome_settings=Options()
chrome_settings.add_argument("--headless") # Run in background without open graphics UI
chrome_settings.add_argument("--no-sandbox") # Bypass OS security model constraints

# Step 2: Boot the automated engine driver instance socket instance cleanly
browser_socket=webdriver.Chrome(options=chrome_settings)

# Step 3: Direct the browser to hit the target URL interface asset
url= "https://news.ycombinator.com/"
browser_socket.get(url)

# Step 4: Extract the fully loaded page source code matrix properties layout
hydrated_html=browser_socket.page_source
print(f"extracted tree size: {len(hydrated_html)} characters.")


# Step 5: Always explicitly tear down the active thread binary socket safely
browser_socket.quit()