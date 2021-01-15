import Souper as sp
import urllib.parse as urlpar

replaceTex = "[myVal1]"

searchURLBase = "https://www.wantedly.com/projects?type=mixed&page=[myVal1]&occupation_types%5B%5D=jp__engineering&hiring_types%5B%5D=mid_career&keywords%5B%5D=%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%82%A2%E3%83%83%E3%83%97&keywords%5B%5D=%E3%83%99%E3%83%B3%E3%83%81%E3%83%A3%E3%83%BC&keywords%5B%5D=%E6%9C%AA%E7%B5%8C%E9%A8%93"

homeUrl = searchURLBase.replace(replaceTex, "1")
searchPage = sp.getSoup(homeUrl)

total = searchPage.find_all("span", class_="total")
totalPages = int(total[0].contents[0])
searchPagesSize = int(totalPages / 10)

searchPages = [searchURLBase.replace(replaceTex, str(i)) for i in range(1,searchPagesSize)]

targetClass = "project-detail"

targets = searchPage.find_all("div", class_=targetClass)

f=open("result.txt","w")
f.write("")
f.close()

for targetPath in searchPages[0:2]:
    searchPage = sp.getSoup(targetPath)
    targets = searchPage.find_all("div", class_=targetClass)
    if len(targets) <= 0:
        break
    vals=""
    for tar in targets:
        title=tar.contents[3].text.replace("\n","")
        href=tar.contents[3].contents[1].attrs["href"]
        uri=urlpar.urljoin(targetPath,href)
        uri=uri[0:uri.find("?")]
        val=title+"\t"+uri
        vals+=val+"\n"
        print(val)
    with open("result.txt","a",encoding="utf-8") as f:
        f.write(vals)



