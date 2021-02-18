from MyFunctions import souper as sp
import urllib.parse as urlpar

import MyFunctions.celeniuming as celen

replaceTex = "page=1"

searchURL = "https://www.wantedly.com/"

saveFile = "./Data/pageUrls.csv"

def loadMarkdHtml():
    with open("Data/Marked.html","r",encoding="utf-8")as f:
        html=f.read()
    return html


def wantedWantedly(searchURLBase):
    html=loadMarkdHtml()

    searchPage = sp.getSoupByHtml(html)

    targetClass = "project"

    targets=searchPage.find_all("div",class_=targetClass)

    f=open(saveFile, "w")
    f.write("")
    f.close()
    vals=""
    for tar in targets:
        titleClass=tar.find("div",class_="project-title")
        title=titleClass.text.replace("\n","").replace(",","")
        href=tar.find_all("a")[0].attrs["href"]

        uri=urlpar.urljoin(searchURLBase,href)
        uri=uri[0:uri.find("?")]
        val=title+","+uri
        vals+=val+"\n"
        print(val)
    with open(saveFile, "a", encoding="utf-8") as f:
        f.write(vals)

def getCompanyThumbnail():
    html=loadMarkdHtml()
    searchPage = sp.getSoupByHtml(html)
    targetClass = "project"
    targets=searchPage.find_all("div",class_=targetClass)

    for tar in targets:
        titleClass=tar.find("div",class_="company-name-wrapper")
        title=titleClass.text.replace("\n","").replace(",","")
        href=tar.find_all("a")[0].attrs["href"]

        uri=href
        uri=uri[0:uri.find("?")]
        val=title+"\t"+uri
        print(val)


if __name__ == '__main__':
    # wantedWantedly(searchURL)
    getCompanyThumbnail()