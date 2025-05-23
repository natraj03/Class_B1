from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("http://65.0.30.232:8090/login?back_url=http%3A%2F%2F65.0.30.232%3A8090%2F")
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("srikanta.bisoyi97@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("Nist@12345")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='global-search--input']").click()
time.sleep(2)

print("click on sign in")