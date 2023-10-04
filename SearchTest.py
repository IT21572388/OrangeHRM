import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSearch():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximizing the window
        self.wait = WebDriverWait(self.driver, 10)  # Explicit wait object

    def teardown_method(self, method):
        self.driver.quit()

    def test_search(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        username_element = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_element.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")

        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button")))
        login_button.click()

        search_box = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-input")))
        search_box.click()
        search_box.send_keys("leave")

        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Leave"))).click()

        time.sleep(4)
