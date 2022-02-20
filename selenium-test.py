from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:5000/form/")

name_input = driver.find_element(By.NAME, "Name")

name_input.clear()
name_input.send_keys("Eve")
name_input.send_keys(Keys.RETURN)

# Adding in a sleep of 3 seconds to make it easier to see the test run
time.sleep(3)

print(driver.current_url)

driver.close()
