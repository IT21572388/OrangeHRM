import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),
    ("InvalidUser2", "InvalidPass2"),

])
def test_login(driver, username, password,):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

    assert "Dashboard" in driver.page_source


