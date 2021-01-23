import webbrowser as wb
import csv
def openMultiPages():

    wb.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"%s')

    with open("./Data/SortedData.csv","r",encoding="utf-8")as f:
        reader=csv.reader(f)
        urls=[]
        for row in reader:
            urls.append(row[0])
        urls=urls[1:]
    openStart=0
    openEnd=20

    for url in urls[openStart:openEnd]:
        #Recommended to run in debug
        url=url.replace("\n","")
        wb.open(url)

if __name__ == '__main__':
    openMultiPages()