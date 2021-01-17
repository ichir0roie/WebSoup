import requests
from bs4 import BeautifulSoup as bs
import time
import random


def getSoup(path):
    res = getHtml(path)
    soup = bs(res.text, "html.parser")
    return soup


def getHtml(path):
    res = requests.get(path)
    time.sleep(random.randint(1, 3))
    return res

def getSoupByHtml(html):
    soup=bs(html,"html.parser")
    return soup

def getSession():
    return requests.session()
