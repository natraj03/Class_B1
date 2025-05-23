from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Chrome()

driver.get("file:///C:/Selenium%20Python/iplticket.html")
time.sleep(2)

# Fill in Name and Surname
driver.find_element(By.NAME, "name").send_keys("Srikanta")
time.sleep(2)
driver.find_element(By.NAME, "surname").send_keys("Bisoyi")
time.sleep(2)

# Date of Birth
driver.find_element(By.NAME, "dob").send_keys("18-10-2002")
time.sleep(2)

# Select Gender
driver.find_element(By.XPATH, "//input[@type='radio']").click()

# Email
driver.find_element(By.NAME, "email").send_keys("srikantabisoyi97@gmail.com")
time.sleep(5)

# Country of Origin
country_dropdown = Select(driver.find_element(By.NAME, "country"))
country_dropdown.select_by_visible_text("India")
time.sleep(5)

# click on checkbox
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
time.sleep(5)

# Click on Submit button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Wait and close
driver.quit()
