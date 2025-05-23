# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# options1 = webdriver.ChromeOptions()
# options1.add_experimental_option("detach",True)
# mydriver = webdriver.Chrome(options=options1)
#
#
# mydriver.get("https://www.amazon.in/")
#
# nameTF = mydriver.find_element(By.ID, "name")
# nameTF.send_keys("Pabitra")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# def openMyproject():
#     driver.get("http://65.0.30.232:8090/projects/5/?jump=angular")
    # http://65.0.30.232:8090/projects/5/?jump=angular
    # time.sleep(5)
def openLoginPage():
    driver.get("http://65.0.30.232:8090/login")
    time.sleep(5)
def username():
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("srikanta.bidoyi97@gmailcom")

def password():
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nist@12345")

def signIn():
    driver.find_element(By.XPATH,"//div[@class='login-form--footer']//input[@name='login']").click()
    time.sleep(5)

def forgetPassword():
    driver.find_element(By.XPATH,"//div[@class='login-links']/a[@href='/account/lost_password']").click()

def createNweAccount():
    driver.find_element(By.XPATH,"//div[@class='login-links']/a[@title='Create a new account']").click()

def openDashboardPage():
    driver.get("http://65.0.30.232:8090/")
    time.sleep(5)
def userMenuLogo():
    driver.find_element(By.XPATH, "//div[@class='op-principal--avatar op-avatar op-avatar_default op-avatar_user op-avatar--fallback']").click()

def signout():
    driver.find_element(By.XPATH,"//a[@class='logout-menu-item op-menu--item-action']").click()

def clickWorkSpace():
    # //a[@id="main-menu-work-packages"]
    driver.find_element(By.XPATH,"//a[@id='main-menu-work-packages']").click()
    time.sleep(5)
def clickCreatebutton():
    # //button[@class="button -alt-highlight add-work-package"]
    driver.find_element(By.XPATH,"//button[@class='button -alt-highlight add-work-package']").click()
    time.sleep(2)
def clickCreatebutton_task():
    # //a[@class="menu-item __hl_inline_type_1"]
    driver.find_element(By.XPATH,"//a[@href='/projects/batch-b1/work_packages/create_new?type=1']").click()