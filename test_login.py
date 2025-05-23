import time
from pages.login import username, password,signIn, openLoginPage

def success():
    openLoginPage()
    username("srikanta.bisoyi97@gmail.com")
    password("Nist@12345")
    signIn()

success()
