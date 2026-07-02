import time  # Built-in library to pause execution if needed
from selenium import webdriver  # Powers the core browser automation
from selenium.webdriver.common.by import By  # Helps locate elements using tags, IDs, or classes
from selenium.webdriver.chrome.options import Options # Allows us to customize how Chrome behaves (like hiding the window)

chrome_options = Options()
chrome_options.add_argument("--headless") # Hides the browser window!
automated_browser = webdriver.Chrome(options=chrome_options)
# Step 1: Initialize an automated Chrome browser window instance


try:
    # Step 2: Instruct the browser to navigate to the target website
    target_url = "http://books.toscrape.com/"
    automated_browser.get(target_url)

    # Step 3: Allow the browser 3 seconds to execute JavaScript and render elements
    time.sleep(3)

    # Step 4: Locate the main store heading using its HTML tag name
    # In Selenium, we find tags using By.TAG_NAME, By.CLASS_NAME, or By.ID
   
    travel_link = automated_browser.find_element(By.LINK_TEXT, "Travel")
    travel_link.click()  # Simulate a click to navigate to the Travel category page
    time.sleep(2)  # Wait for the new page to load after clicking the link
    
    main_heading_element = automated_browser.find_element(By.TAG_NAME, "h1")
    # Step 5: Extract the visible text inside that element
    page_title = main_heading_element.text
    print(f"Scraped Title via Selenium: {page_title}")

finally:
    # Step 6: ALWAYS close the automated browser window when done, even if errors occur
    automated_browser.quit()

