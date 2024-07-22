from pprint import pprint

positions = ["PRESIDENT", "TREASURER", "DIRECTOR", "SECRETARY"]
label=["Association Name", "# of Units", "Board Title", "Full Name", "Address", "City", "State", "Zip"]
cities=[]
with open("C:/Users/yhk13/OneDrive/Documents/Condoly-Projects/DataCollection/Cities.txt", "r") as temp:
    for line in temp:
        cities.append(line[:-1])
    temp.close()
omit=[]
with open("C:/Users/yhk13/OneDrive/Documents/Condoly-Projects/DataCollection/omit.txt", "r") as temp:
    for line in temp:
        omit.append(line[:-1].upper())
    temp.close()
for i in omit:
    print(i)
data=[]
with open("C:/Users/yhk13/OneDrive/Documents/Condoly-Projects/DataCollection/finalList.txt", "r") as temp:
    info={}
    cnt=0
    skip=False
    for line in temp:
        if (line=="\n"):
            skip=False
            cnt=0
            if (info=={}):
                continue
            data.append(info)
            info={}
        else:
            if (skip):
                continue
            cnt+=1
            curr=line[:-1].split()
            if (info=={}):
                # if (cnt<30):
                #     print(line[9:-1])
                if (line[9:-1] in omit):
                    # print(line[9:-1])
                    skip=True
                    continue
                info["Association Name"]=line[9:-1]
            elif (curr[0] in positions):
                if (not("Board Title" in info.keys())):
                    info["Board Title"]=[]
                    info["Full Name"]=[]
                    info["Address"]=[]
                    info["City"]=[]
                    info["State"]=[]
                    info["Zip"]=[]
                name=""
                stop=len(curr[0])
                for i in range(1, len(curr)):
                    if (curr[i][0].isnumeric()):
                        break
                    name+=" "+curr[i]
                    stop+=1+len(curr[i])
                stop+=1
                if (name[1:] in info["Full Name"]):
                    continue
                info["Full Name"].append(name[1:])
                info["Board Title"].append(curr[0])
                

                address=line[stop:-1]
                found=False
                for city in cities:
                    if (address.rfind(" "+city+" ")==-1):
                        continue
                    else:
                        info["City"].append(city)
                        address=address[:address.rfind(" "+city+" ")]
                        found=True
                        break
                if (not found):
                    info["City"].append("")
                    info["State"].append("")
                found=False
                if (info["City"][-1]!=""):
                    ind=line.rfind(" "+info["City"][-1]+" ")+len(info["City"][-1])
                    currInd=len(curr[0])
                    for i in range(1, len(curr)):
                        if (currInd>=ind and not(curr[i].isnumeric())):
                            info["State"].append(curr[i])
                            found=True
                            break
                        currInd+=1+len(curr[i])
                if (not found):
                    info["State"].append("")
                info["Address"].append(address)
                if (curr[-1][:5].isnumeric()):
                    info["Zip"].append(curr[-1][:5])
                else:
                    info["Zip"].append("")
            elif (curr[0]=="UNITS:"):
                if (len(curr)==1):
                    info["# of Units"]="0"
                else:
                    info["# of Units"]=curr[1]
    temp.close()
# pprint(data)
with open("C:/Users/yhk13/OneDrive/Documents/Condoly-Projects/DataCollection/finalListExcel.csv", "w") as temp:
    for i in range(len(label)):
        if (i==len(label)-1):
            temp.write(label[i]+"\n")
        else:
            temp.write(label[i]+",")
    for info in data:
        for ind in range(0, len(info["Board Title"])):
            for i in range(len(label)):
                if (i==len(label)-1):
                    temp.write(info[label[i]][ind]+"\n")
                else:
                    if (not(label[i]) in info.keys()):
                        temp.write(",")
                    elif (label[i]=="Board Title" or label[i]=="Full Name" or label[i]=="City" or label[i]=="Address" or label[i]=="Zip" or label[i]=="State"):
                        temp.write(info[label[i]][ind]+",")
                    else:
                        temp.write(info[label[i]]+",")
    temp.close()