from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from POM.pages import LoginPage
from POM.pages.DeletePage import DeletePage

def delete_test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Using the LoginPage class
    login_page = LoginPage.LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    time.sleep(3)
    login_page.click_login()

    # Using the DeletePage class
    delete_page = DeletePage(driver)
    delete_page.click_menu_item()
    delete_page.click_table_card_button()
    delete_page.click_danger_label_button()

    time.sleep(4)
    driver.quit()

if __name__ == "__main__":
    delete_test()
