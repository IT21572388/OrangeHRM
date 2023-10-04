from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Increased the wait time to 20 seconds for illustration

    def click_menu_item(self):
        menu_item_wrapper_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper:nth-child(1) .oxd-text")))
        menu_item_wrapper_button.click()

    def click_table_card_button(self):
        table_card_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(1)")))
        table_card_button.click()

    def click_danger_label_button(self):
        try:
            danger_label_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-button--label-danger")))
            danger_label_button.click()
        except TimeoutException:
            self.driver.save_screenshot('error_screenshot.png')
            raise
