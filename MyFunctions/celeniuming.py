import time
from selenium import webdriver

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

    return driver


if __name__=="__main__":
    getLoggedDriver()