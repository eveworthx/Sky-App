from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:5000/form/")

name_input = driver.find_element(By.NAME, "Name")

name_input.clear()
name_input.send_keys("Eve")

submit_button = driver.find_element(By.CLASS_NAME, "submit-btn")
submit_button.click()

# Look for paragraph element on success page
name_result = driver.find_element(By.CLASS_NAME, "success-message")

# Testing whether the name entered into the form is correct
assert name_result.text == "Thanks Eve"

print(driver.current_url)

driver.close()
