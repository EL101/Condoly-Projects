data1=[]
data2=[]
def readData(file, data):
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly-Projects/DataCollection/"+file, "r") as temp:
        curr={}
        for line in temp:
            L=line[:-1].split(": ")
            if (line=="\n"):
                data.append(curr)
                # if (len(data)<=30):
                #     print(curr)
                curr={}
            elif (len(L)==2):
                curr[L[0]]=L[1]
            else:
                curr[L[0]]=''
        temp.close()
readData("data.txt", data1)
readData("data_excel.txt", data2)
def findMatch():
    matches=[]
    for info in data1:
        ind=-1
        for i in range(0, len(data2)):
            info2=data2[i]
            if (info["ZIPCODE"]==info2["ZIPCODE"] and (info["STR_NAME"]==info2["STR_NAME"])):
                curr={}
                label=["POSITION", "DIR", "STR_NAME", "(STR_SUFF)", "CITY_NAME", "ZIPCODE", "UNITS"]
                for s in label:
                    if (info[s]==''):
                        curr[s]=info2[s]
                    else:
                        curr[s]=info[s]
                matches.append(curr)
                ind=i
                break
        if (ind!=-1):
            data2.remove(data2[ind])
    return matches
def writeOut(matches):
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly-Projects/DataCollection/matches.txt", "w") as temp:
        for info in matches:
            for i in info.keys():
                temp.write(i+": "+info[i]+"\n")
            temp.write("\n")
writeOut(findMatch())
