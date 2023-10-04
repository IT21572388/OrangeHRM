import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEditTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)  # I kept it 20s as earlier

    def teardown_method(self, method):
        self.driver.quit()

    def test_editTest(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        # Login steps
        username_element = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_element.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button")))
        login_button.click()

        # Wait for the body element to be present
        body_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))


        actions = ActionChains(self.driver)
        actions.move_to_element(body_element).perform()

        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(body_element, 0, 0).perform()

        # Clicking on "My Info" link
        my_info_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My Info")))
        my_info_link.click()


        time.sleep(2)

        my_info_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My Info")))
        actions = ActionChains(self.driver)
        actions.move_to_element(my_info_link).perform()
        self.wait = WebDriverWait(self.driver, 20)

        my_info_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My Info")))
        my_info_link.click()


        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".known-element-after-myinfo")))


        try:
            focus_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-input--focus")))
        except TimeoutException:
            focus_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-input--focus")))
        focus_input.click()
        focus_input.send_keys("Nicky am nick")

        # Click the button
        secondary_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button--secondary:nth-child(2)")))
        secondary_button.click()
