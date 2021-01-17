import webbrowser as wb

wb.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"%s')

with open("./Data/urlsForOpen.txt","r",encoding="utf-8")as f:
    urls=f.readlines()

openStart=0
openEnd=20

for url in urls[openStart:openEnd]:
    url=url.replace("\n","")
    wb.open(url)
