import webbrowser as wb

def openMultiPages():

    wb.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"%s')

    with open("./Data/urlsForOpen.txt","r",encoding="utf-8")as f:
        urls=f.readlines()

    openStart=0
    openEnd=20

    for url in urls[openStart:openEnd]:
        #Recommended to run in debug
        url=url.replace("\n","")
        wb.open(url)

if __name__ == '__main__':
    openMultiPages()