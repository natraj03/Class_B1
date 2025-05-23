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

