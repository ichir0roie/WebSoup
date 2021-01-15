import requests
from bs4 import BeautifulSoup as bs
import time
import random

def getSoup(path):
    res = requests.get(path)
    time.sleep(random.randint(1,3))
    soup = bs(res.text, "html.parser")
    return soup
