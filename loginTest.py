from telnetlib import EC

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/")
username_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_element.send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".oxd-button").click() ##using css selector , bcz it cant directry find.

time.sleep(2)

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
#
# ==================================

driver.maximize_window() ##use to maximize the browser window

links=driver.find_elements(By.TAG_NAME, 'a') #using multiple locators
print(len(links))

time.sleep(2)
driver.close()
