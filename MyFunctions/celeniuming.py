import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import random

with open("./Data/loginInfo","r",encoding="utf-8")as f:
    mail=f.readline().replace("\n","")
    paWd=f.readline().replace("\n","")

loginPath = "https://www.wantedly.com/signin_or_signup?step=SigninOrSignup&email="+mail.replace("@","%40")

def getLoggedDriver():
    driver = webdriver.Chrome("./Data/chromedriver.exe")
    driver.get(loginPath)

    time.sleep(1)

    ipPW = driver.find_element_by_name("password")
    ipPW.send_keys(paWd)

    btSubmit = driver.find_element_by_id("next-step-button")
    btSubmit.click()

    time.sleep(random.randint(1, 2))
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "new-ui-modal-full-page-wrapper")))
    except TimeoutException as te:
        print("can't get page")

    return driver

if __name__=="__main__":
    getLoggedDriver()