label=["POSITION", "DIR", "STR_NAME", "(STR_SUFF)", "CITY_NAME", "ZIPCODE", "UNITS"]
index=[-1, 7, 8, 9, 10, 11, 2]
data=[]
with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/excelCondos.txt", "r") as temp:
    for line in temp:
        curr=line[:-1].split(',')
        info={}
        for i in range(len(label)):
            if (index[i]==-1):
                info[label[i]]=''
            else:
                if (label[i]=="ZIPCODE"):
                    info[label[i]]=curr[index[i]][:5]
                else:
                    info[label[i]]=curr[index[i]]
        data.append(info)
    temp.close()
with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/data_excel.txt", "w") as temp:
    for info in data:
        for s in label:
            temp.write(s+": "+info[s]+"\n")
        temp.write("\n")
    temp.close()
