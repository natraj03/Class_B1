from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Open local HTML form
driver.get("file:///C:/Selenium%20Python/seleniumForm1.html")
time.sleep(2)

# Step 3: Fill out the form
driver.find_element(By.ID,"name").send_keys("Srikanta")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "Srikanta12").send_keys("Bisoyi")
time.sleep(1)

# Select gender
driver.find_element(By.NAME, "gender").click()  # or "female"
time.sleep(1)

driver.find_element(By.ID, "address123").send_keys("Pratapur, Berhampur, Ganjam, Odisha")
time.sleep(1)

driver.find_element(By.NAME, "dob").send_keys("18-10-2002")
time.sleep(1)

# Select country
Select(driver.find_element(By.ID, "country123")).select_by_visible_text("India")
time.sleep(1)

# Tick checkbox
driver.find_element(By.NAME, "agree").click()
time.sleep(1)

# Click Submit
driver.find_element(By.ID, "1234").click()
time.sleep(2)

# Done
print("Form submitted successfully!")
driver.quit()
