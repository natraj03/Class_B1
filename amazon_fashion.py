from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options1 = webdriver.ChromeOptions()
options1.add_experimental_option("detach",True)
mydriver = webdriver.Chrome(options=options1)


mydriver.get("https://www.amazon.in/gp/browse.html?node=6648217031&ref_=nav_cs_fashion")