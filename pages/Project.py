from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v134.fed_cm import click_dialog_button
from selenium.webdriver.support.ui import Select
import time

# Step 1: Open browser
driver = webdriver.Chrome()

def openLoginPage():
    driver.get("http://65.0.30.232:8090/login")

def username(username):
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)

def password(password):
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

def signIn():
    driver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()

def dash_board():
    driver.get("http://65.0.30.232:8090/my/page")

def Click_on_project():
    driver.find_element(By.XPATH,"//span[@class='op-app-menu--item-title ellipsis']").click()

def Batch_B1():
    driver.find_element(By.XPATH,"//a[contains(@class, 'spot-list--item-action')]//span[contains(@class, 'spot-list--item-title') and contains(text(), 'Batch_B1')]").click()

def Work_Packages():
    driver.find_element(By.XPATH,"//a[@id='main-menu-work-packages']").click()

def Create_a_Task():
    driver.find_element(By.XPATH,"//a[@class='menu-item __hl_inline_type_1']//span[text()='Task']").click()

def click_on_Create():
    driver.find_element(By.XPATH, "//span[text()='Create']").click()

def Create_a_Task():
    driver.find_element(By.XPATH, "//a[@class='menu-item __hl_inline_type_1']//span[text()='Task']").click()

def fill_New_Task(NewTask):
    driver.find_element(By.XPATH, "//input[@id='wp-new-inline-edit--field-subject']").send_keys(NewTask)

def fill_Paragraph(Paragraph):
    driver.find_element(By.XPATH, "//p[@class='op-uc-p']").send_keys(Paragraph)
