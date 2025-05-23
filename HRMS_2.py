from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1: Open browser
driver = webdriver.Chrome()

# Step 2: Open local HTML form
driver.get("file:///C:/Selenium%20Python/seleniumForm1.html")
time.sleep(2)

# Step 3: Fill out the form using simple XPath expressions

# Name
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Srikanta")
time.sleep(1)

# Surname
driver.find_element(By.XPATH, "//input[@name='surname']").send_keys("Bisoyi")
time.sleep(1)

# Gender (Male)
driver.find_element(By.XPATH, "//input[@value='male']").click()
time.sleep(1)

# Address
driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Pratapur, Berhampur, Ganjam, Odisha")
time.sleep(1)

# Date of Birth
driver.find_element(By.XPATH, "//input[@id='dob']").send_keys("2002-10-18")
time.sleep(1)

# Country (India)
Select(driver.find_element(By.XPATH, "//select[@id='country']")).select_by_visible_text("India")
time.sleep(1)

# Agree to terms
driver.find_element(By.XPATH, "//input[@id='agree']").click()
time.sleep(1)

# Submit button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

print("Form submitted successfully!")
driver.quit()
