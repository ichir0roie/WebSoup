import webbrowser as wb
import csv


def openMultiPages():

    wb.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"%s')

    with open("./Data/SortedElementsData.csv","r",encoding="utf-8")as f:
        reader=csv.reader(f)
        urls=[]
        for row in reader:
            urls.append(row[0])
        urls=urls[1:]
    openStart=20
    openEnd=20

    for url in urls[openStart:]:
        #Recommended to run in debug
        url=url.replace("\n","")
        wb.open(url)

import glob
localFolderPath="Data/Htmls/*"
def openMultiPagesOnFolder():
    files=glob.glob(localFolderPath)
    for i in files:
        wb.open(i)

def openMultiPagesFromUrls():
    wb.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"%s')

    with open("./Data/targetUrls.txt","r",encoding="utf-8")as f:
        reader=f.readlines()

    for url in reader:
        # Recommended to run in debug
        url = url.replace("\n", "")
        wb.open(url)


if __name__ == '__main__':
    # openMultiPages()
    # openMultiPagesOnFolder()
    openMultiPagesFromUrls()