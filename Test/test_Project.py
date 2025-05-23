import time
from pages.login import *
from pages.Project import *


def test_success():
    openLoginPage()
    username("srikanta.bisoyi97@gmail.com")
    password("Nist@12345")
    signIn()

def test_Click2():
    Click_on_project()
    Batch_B1()
    Work_Packages()
    Create_a_Task()
    fill_New_Task()
    fill_Paragraph()

