import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddEmployee:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximizing the window
        self.wait = WebDriverWait(self.driver, 20)  # Increased Explicit wait to 20 seconds

    def teardown_method(self, method):
        self.driver.quit()

    def test_realAdd(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # Login steps
        username_element = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_element.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button")))
        login_button.click()

        admin_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin")))
        admin_link.click()
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button--secondary:nth-child(1)")))
        button.click()

        select_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-select-text--focus > .oxd-select-text-input")))
        select_input.click()

        autocomplete_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")))
        autocomplete_input.click()
        autocomplete_input.send_keys("Fiona  Grace")

        select_text_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-select-text--focus > .oxd-select-text-input")))
        select_text_input.click()

        oxd_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-input--focus")))
        oxd_input.click()
        oxd_input.send_keys("fiona1")
        oxd_input.click()
        oxd_input.send_keys("iloveyouamma1")
        oxd_input.click()
        oxd_input.send_keys("iloveyouamma1")

        save_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button--secondary")))
        save_button.click()
