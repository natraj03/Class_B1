from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_empty():
     driver.get("http://65.0.30.232:8090/login")  # Load page directly
     driver.find_element(By.XPATH, "//div[@class='login-form--footer']//input[@name='login']").click()
     time.sleep(2)

def test_invalid():
    driver.get("http://65.0.30.232:8090/login")  # Load page directly
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("srikanta.bisoyi977@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")
    driver.find_element(By.XPATH, "//div[@class='login-form--footer']//input[@name='login']").click()
    time.sleep(2)

def test_success():
    driver.get("http://65.0.30.232:8090/login")
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("srikanta.bisoyi97@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")
    driver.find_element(By.XPATH, "//div[@class='login-form--footer']//input[@name='login']").click()
    time.sleep(2)

def test_Signout():
    driver.get("http://65.0.30.232:8090/login")
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("srikanta.bisoyi97@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")
    driver.find_element(By.XPATH, "//div[@class='login-form--footer']//input[@name='login']").click()
    driver.find_element(By.XPATH,"//opce-principal[@class='op-top-menu-user-avatar op-principal']/div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[@class='logout-menu-item op-menu--item-action']/span[@class='op-menu--item-title']/span[@class='ellipsis']").click()
    time.sleep(2)

test_empty()
test_invalid()
test_success()
test_Signout()
time.sleep(2)

driver.quit()
