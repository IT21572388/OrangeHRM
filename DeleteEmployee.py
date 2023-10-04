import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDeletemployee:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximizing the window
        self.wait = WebDriverWait(self.driver, 20)  # Increased Explicit wait to 20 seconds

    def teardown_method(self, method):
        self.driver.quit()

    def test_deleteEmployee(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # Login steps
        username_element = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_element.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button")))
        login_button.click()

    def test_deleteEmployee(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # Login steps
        username_element = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_element.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button")))
        login_button.click()

        menu_item_wrapper_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper:nth-child(1) .oxd-text")))
        menu_item_wrapper_button.click()

        # Click on the table card button
        table_card_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(1)")))
        table_card_button.click()

        # Click on the danger label button
        danger_label_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button--label-danger")))
        danger_label_button.click()

        time.sleep(4)

