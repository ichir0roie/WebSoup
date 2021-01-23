from  janome.tokenizer import Tokenizer

import MyFunctions.souper as sp

import glob

import csv

import  unicodedata

def getHtmlPaths():
    files=glob.glob("Data/Htmls/*.html")
    return files

def getHtmlTextFromPath(path):
    htmlText=""
    with open(path,"r",encoding="utf-8")as f:
        htmlText=f.read()
    return htmlText


def getTokenFromHtml(htmlText):
    soup=sp.getSoupByHtml(htmlText)
    text=soup.text.replace("\n","")

    sentences=torkenizer.tokenize(text)
    tokens=[t for t in sentences]
    return tokens

def getAllTokenAndSave():
    files=getHtmlPaths()
    csvList=[]
    for c,i in enumerate(files):
        print(c)
        tokens=getTokenFromHtml(getHtmlTextFromPath(i))
        for i in tokens:
            val=str(i).replace("\t",",")
            if "名詞" in val:
                val=val.split(",")[0]
                Find=False
                for c,data in enumerate(csvList):
                    if val in data:
                        csvList[c][1]+=1
                        Find=True
                        break
                if not Find:
                    csvList.append([val,0])

        print("nowLen:"+str(len(csvList)))


    with open("Data/Token.csv","w",encoding="utf-8")as f:
        writer=csv.writer(f)
        writer.writerows(csvList)

def RemoveEnter():
    with open("Data/Token.csv","r",encoding="utf-8")as f:
        d=f.readlines()
    with open("Data/Token.csv","w",encoding="utf-8",newline="")as f:
        for i in d:
            if len(i)>1:
                f.write(i)


import pandas as pd

def searchModernTech():
    with open("Data/Token.csv","r",encoding="utf-8")as f:
        reader=csv.reader(f)

        data=[]
        for i in reader:
            data.append(i)

    next=[]
    for i in data:
        alpha=True
        for char in i[0]:
            if not unicodedata.east_asian_width(char)=="Na":
                alpha=False
                break
        if alpha:
            next.append(i)

    df=pd.DataFrame(next,columns=["val","count"])
    df["count"]=df["count"].astype(int)
    print(df)
    df=df.sort_values("count",ascending=False)
    df.to_csv("Data/TokenPD.csv")
    #
    # with open("Data/TokenSearch.csv","w",encoding="utf-8" ,newline="")as f:
    #     writer=csv.writer(f)
    #     writer.writerows(next)

torkenizer=None
if __name__ == '__main__':
    torkenizer=Tokenizer()


    #getAllTokenAndSave()
    #RemoveEnter()

    searchModernTech()
