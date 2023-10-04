from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from POM.pages import LoginPage


def test_login_flow():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Using the LoginPage class
    login_page = LoginPage.LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    time.sleep(3)
    login_page.click_login()

    time.sleep(2)

if __name__ == "__main__":
    test_login_flow()


