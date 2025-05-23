from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Chrome()

def setup_function():
    driver.get("http://65.0.30.232:8090/login")
    time.sleep(5)


def test_invalidCredentilas():
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("1Rashmiranjan4546@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")
    driver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()


def test_success():
    # time.sleep(5)
    # mydriver.get("http://65.0.30.232:8090/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Rashmiranjan4546@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")
    driver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()

