import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import random

import os

def targetPageHtmlGetter():
    with open("./Data/pageUrls.csv", "r", encoding="utf-8")as f:
        reader = csv.reader(f)
        targetUrls=[row for row in reader]

    from MyFunctions import celeniuming

    driver= celeniuming.getLoggedDriver()

    driver.get("https://www.wantedly.com/projects/")
    time.sleep(random.randint(1,5))

    if not os.path.exists("Data/Htmls"):
        os.mkdir("Data/Htmls")

    startPlace=0

    for c,tar in enumerate(targetUrls[startPlace:]):
        name=tar[0].replace(" ","")\
            .replace("\n","")\
            .replace("\u3000","")\
            .replace("|","")\
            .replace("/","")\
            .replace(".","。")\
            .replace("！","")\
            .replace("?","")\
            .replace("\"","")
        url=tar[1]

        print(name)
        print(url)

        driver.get(url)

        time.sleep(random.randint(1,2))
        try:
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CLASS_NAME,"js-descriptions ")))
        except TimeoutException as te:
            print("can't get page")
            print(name)
            print(url)
            print("++++++++++++++++++++++++++\n")
            continue
        print(c+startPlace)
        html=driver.page_source
        with open("./Data/Htmls/"+name+".html","w",encoding="utf-8")as f:
            f.write(html)


if __name__ == '__main__':
    targetPageHtmlGetter()


