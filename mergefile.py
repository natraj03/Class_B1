from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.devtools.v134.fed_cm import click_dialog_button
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time

# Step 1: Open browser
driver = webdriver.Chrome()


def openLoginPage():
    driver.get("http://65.0.30.232:8090/login")
    time.sleep(2)
def username():
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("srikanta.bisoyi97@gmail.com")
    time.sleep(2)

def password():
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")
    time.sleep(2)

def signIn():
    driver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()
    time.sleep(2)

def Click_on_project():
    driver.find_element(By.XPATH,"//span[@class='op-app-menu--item-title ellipsis']").click()
    time.sleep(2)

def Batch_B1():
    # driver.find_element(By.XPATH,"//a[@class='spot-list--item-action spot-list--item-action_active']//span[@class='spot-list--item-title spot-list--item-title_ellipse-text']").click
    driver.find_element(By.XPATH,"//a[contains(@class, 'spot-list--item-action')]//span[contains(@class, 'spot-list--item-title') and contains(text(), 'Batch_B1')]").click()
    time.sleep(2)

def Work_Packages():
    # driver.find_element(By.XPATH,"//span[@class='op-menu--item-title']//span[contains(text(), 'Work')]").click()
    driver.find_element(By.XPATH, "//a[@id='main-menu-work-packages']").click()
    time.sleep(2)

def click_on_Create():
    driver.find_element(By.XPATH,"//span[text()='Create']").click()
    time.sleep(2)

def Create_a_Task():
    driver.find_element(By.XPATH,"//a[@class='menu-item __hl_inline_type_1']//span[text()='Task']").click()
    time.sleep(2)

def fill_New_Task():
    driver.find_element(By.XPATH,"//input[@id='wp-new-inline-edit--field-subject']").send_keys("Srikanta_New_Project")
    time.sleep(2)

def fill_Paragraph():
    driver.find_element(By.XPATH,"//p[@class='op-uc-p']").send_keys("it's my new project")
    time.sleep(2)
def Choose_Assignee():
    driver.find_element(By.XPATH,"")

openLoginPage()
username()
password()
signIn()
Click_on_project()
Batch_B1()
Work_Packages()
click_on_Create()
Create_a_Task()
fill_New_Task()
fill_Paragraph()
time.sleep(2)

