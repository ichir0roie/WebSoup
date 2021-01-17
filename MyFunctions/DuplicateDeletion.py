

with open("./Data/pageUrls.csv","r",encoding="utf-8")as f:
    data=f.readlines()

outputData=[]
befId="0"
for i in data:
    id=i[-6:]
    if id==befId:
        continue
    outputData.append(i)
    befId=i[-6:]

print(outputData)


with open("./Data/pageUrls.csv","w",encoding="utf-8")as f:
    f.writelines(outputData)

