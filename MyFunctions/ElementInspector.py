import glob
from MyFunctions import souper as sp

inputDataPath="./Data/Htmls/*"
files=glob.glob(inputDataPath)

outputDataPath="./Data/ElementsData.csv"
delimiter=","

startPlace=116
for c,page in enumerate(files[startPlace:]):
    print(c+startPlace)
    with open(page,"r",encoding="utf-8")as f:
        html=f.read()
    soup=sp.getSoupByHtml(html)

    text=soup.text

    urls=soup.find_all("link",hreflang="ja-jp",rel="alternate")[0]
    url=urls.attrs["href"]

    title=soup.find(class_="project-title new-style")
    if title is None:
        title = soup.find(class_="project-title")
    if title is not None:
        title=title.text.replace("\n","").replace(",","").replace("、","")
    else:
        title="can't get!!"


    name=soup.find(class_="new-style company-link")
    if name is None:
        name = soup.find(class_="company-name")
    if name is not None:
        name=name.text.replace("\n","").replace(",","").replace("、","")
    else:
        name="can't get!!"

    membersSearch=soup.find_all("div",class_="company-description")
    for i in membersSearch:
        if "人のメンバー" in i.text:
            members=i.text.replace("\n","").replace("人のメンバー","")
            break


    searchKeywords=[
        "react",
        "node",
        "rails",
        "python",
        "音楽",
        "未経験",
        "web",
        "ベンチャー",
        "スタートアップ",
    ]

    hitsKeyWords=[]
    for i in searchKeywords:
        if i.lower() in text.lower():
            hitsKeyWords.append(i)
    outText=""
    outText+=url+delimiter
    outText+=name+delimiter
    outText+=title+delimiter
    outText+=members+delimiter
    for i in hitsKeyWords:
        outText+=i+delimiter
    outText+="\n"
    with open(outputDataPath,"a",encoding="utf-8")as f:
        f.write(outText)

