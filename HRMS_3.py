# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# # Launch the browser
# driver = webdriver.Chrome()
#
# # Load the local HTML file
# driver.get("file:///C:/Users/LENOVO/AppData/Local/Microsoft/Windows/INetCache/IE/NVLXXA0N/iplticket[1].html")
# time.sleep(2)
#
# # Fill Name
# driver.find_element(By.XPATH, "//label[contains(text(), 'Name')]/input").send_keys("Srikanta")
# time.sleep(1)
#
# # Fill Surname
# driver.find_element(By.XPATH, "//label[contains(text(), 'Surname')]/input").send_keys("Bisoyi")
# time.sleep(1)
#
# # Date of Birth
# driver.find_element(By.XPATH, "//label[contains(text(), 'Date of Birth')]/input").send_keys("2002-10-18")
# time.sleep(1)
#
# # Select Gender - Male
# driver.find_element(By.XPATH, "//input[@type='radio' and @value='male']").click()
# time.sleep(1)
#
# # Email
# driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/input").send_keys("srikanta@example.com")
# time.sleep(1)
#
# # Country - Select India
# Select(driver.find_element(By.XPATH, "//select[@id='select-country']")).select_by_visible_text("India")
# time.sleep(1)
#
# # Agree to terms
# driver.find_element(By.XPATH, "//input[@id='checkbox-agree']").click()
# time.sleep(1)
#
# # Increase members for Match 1 to 2
# for _ in range(2):
#     driver.find_element(By.XPATH, "//tr[@id='match-1-row']//button[contains(text(), '+')]").click()
#     time.sleep(1)
#
# # Increase members for Match 2 to 1
# driver.find_element(By.XPATH, "//tr[@id='match-2-row']//button[contains(text(), '+')]").click()
# time.sleep(1)
#
# # Submit the form
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(2)
#
# print("IPL Match Registration Form submitted successfully.")
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch the browser once
driver = webdriver.Chrome()

def test_fill_IPL_Form():
    # Load the local HTML file
    driver.get("file:///C:/Users/LENOVO/AppData/Local/Microsoft/Windows/INetCache/IE/NVLXXA0N/iplticket[1].html")
    time.sleep(2)

    # Fill Name
    driver.find_element(By.XPATH, "//label[contains(text(), 'Name')]/input").send_keys("Srikanta")
    time.sleep(1)

    # Fill Surname
    driver.find_element(By.XPATH, "//label[contains(text(), 'Surname')]/input").send_keys("Bisoyi")
    time.sleep(1)

    # Date of Birth
    driver.find_element(By.XPATH, "//label[contains(text(), 'Date of Birth')]/input").send_keys("2002-10-18")
    time.sleep(1)

    # Select Gender - Male
    driver.find_element(By.XPATH, "//input[@type='radio' and @value='male']").click()
    time.sleep(1)

    # Email
    driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/input").send_keys("srikanta@example.com")
    time.sleep(1)

    # Country - Select India
    Select(driver.find_element(By.XPATH, "//select[@id='select-country']")).select_by_visible_text("India")
    time.sleep(1)

    # Agree to terms
    driver.find_element(By.XPATH, "//input[@id='checkbox-agree']").click()
    time.sleep(1)

    # Increase members for Match 1 to 2
    for _ in range(2):
        driver.find_element(By.XPATH, "//tr[@id='match-1-row']//button[contains(text(), '+')]").click()
        time.sleep(1)

    # Increase members for Match 2 to 1
    driver.find_element(By.XPATH, "//tr[@id='match-2-row']//button[contains(text(), '+')]").click()
    time.sleep(1)

    # Submit the form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    print("IPL Match Registration Form submitted successfully.")

# Run the function
test_fill_IPL_Form()

# Close the browser
driver.quit()
