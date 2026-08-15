from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationcentral.com/demo/#google_vignette")

# Wait until the element is present in the DOM
my_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="date_picker.html"]'))
)

# Scroll into view (helps if it's off-screen)
driver.execute_script("arguments[0].scrollIntoView();", my_element)

# Force click with JavaScript (bypasses 'not interactable' issue)
driver.execute_script("arguments[0].click();", my_element)
