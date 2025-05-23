import time
from pages.login import username, password,signIn, openLoginPage,Click_on_project,Batch_B1,Work_Packages,Create_a_Task

def success():
    openLoginPage()
    username("srikanta.bisoyi97@gmail.com")
    password("Nist@12345")
    signIn()

def Click2():
    Click_on_project()
    Batch_B1()
    Work_Packages()
    Create_a_Task()

success()
Click2()