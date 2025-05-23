from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment to run without opening browser
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # ✅ Use Service() with path to chromedriver
    service = Service("/Users/apple/Documents/chromedriver/14chromedriver_mac64/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    return driver

def openMyFirstLink():
    driver = create_driver()
    print("Chechk drivweerr", driver)
    driver.maximize_window()
    driver.get("https://google.com")



openMyFirstLink()