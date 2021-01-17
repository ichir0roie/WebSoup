from MyFunctions import souper as sp
import urllib.parse as urlpar

replaceTex = "page=1"

searchURLBase = "https://www.wantedly.com/projects?type=mixed&page=1&occupation_types%5B%5D=jp__engineering&hiring_types%5B%5D=mid_career&keywords%5B%5D=%E9%9F%B3%E6%A5%BD"

#homeUrl = searchURLBase.replace(replaceTex, "1")
searchPage = sp.getSoup(searchURLBase)

total = searchPage.find_all("span", class_="total")
totalPages = int(total[0].contents[0])
searchPagesSize = int(totalPages / 10)

searchPages = [searchURLBase.replace(replaceTex, "page="+str(i)) for i in range(1,searchPagesSize)]

targetClass = "project-detail"

targets = searchPage.find_all("div", class_=targetClass)

saveFile="./Data/pageUrls.csv"
f=open(saveFile, "w")
f.write("")
f.close()

for targetPath in searchPages:
    searchPage = sp.getSoup(targetPath)
    targets = searchPage.find_all("div", class_=targetClass)
    if len(targets) <= 0:
        break
    vals=""
    for tar in targets:
        title=tar.contents[3].text.replace("\n","").replace(",","")
        href=tar.contents[3].contents[1].attrs["href"]
        uri=urlpar.urljoin(targetPath,href)
        uri=uri[0:uri.find("?")]
        val=title+","+uri
        vals+=val+"\n"
        print(val)
    with open(saveFile, "a", encoding="utf-8") as f:
        f.write(vals)


