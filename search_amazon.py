from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
myService = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
mydriver = webdriver.Chrome(service=myService, options= options)

mydriver.get("https://google.com")
# mydriver.find_element(By.XPATH, '//textarea[@id="APjFqb"]').send_keys("amazon", Keys.RETURN)
mydriver.find_element(By.XPATH, '//textarea[@id="APjFqb"]').send_keys("myntra", Keys.RETURN)

time.sleep(20)
# mydriver.find_element(By.XPATH,'//span[@class="V9tjod"]/a[@href="https://www.amazon.in/"]').click()

mydriver.find_element(By.XPATH,'//span[@class="V9tjod"]/a[@href="https://www.myntra.com/"]').click()

time.sleep(5)
mydriver.find_element(By.XPATH,'//input[@class="desktop-searchBar"]').send_keys("beauty",Keys.RETURN)

