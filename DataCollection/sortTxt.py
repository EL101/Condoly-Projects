file = open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/CDB29AJ-Condominium-List.TXT", "r")

directions = ["NORTH", "EAST", "SOUTH", "WEST", "N.", "E.", "S.", "W.", "N", "E", "S", "W"]
positions = ["PRESIDENT", "TREASURER", "DIRECTOR", "SECRETARY"]
suff = ["AVE", "RD", "CT", "BLVD", "ST", "DR", "HWY", "PL", "PKWY", "LN", "WAY", "TER", "TRL", "CIR", "WALK", "SQ", "PKY", "PLZ", "PARK", "STREET"]
city_names = []
with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/Cities.txt") as temp:
    for line in temp:
        bnd=len(line)
        if (line[-1]=='\n'):
            bnd-=1
        city_names.append(line[:bnd])
    temp.close()
str_names = []
with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/Street_Names.txt") as temp:
    for line in temp:
        bnd=len(line)
        if (line[-1]=='\n'):
            bnd-=1
        str_names.append(line[:bnd])
    temp.close()
# print(str_names)
label=["POSITION", "DIR", "STR_NAME", "(STR_SUFF)", "CITY_NAME", "ZIPCODE", "UNITS"]
data =[]
cnt=0
for line in file:
    # if (cnt>30):
    #     break
    curr=line.split()
    #headers for each page not needed
    if ("6/12/24" in curr or "OD" in curr):
        continue

    #cleaning up data
    if (len(curr)>0 and (curr[0]=='-' or curr[0]=='0')):
        curr.remove(curr[0])
    if (len(curr)==0):
        continue
    if (not (curr[0] in positions)):
        continue
    #format data
    newLine=""
    for s in curr:
        newLine+=" "+s
    newLine=newLine[1:]
    
    info={}
    for s in label:
        info[s]=''
    info["POSITION"]=curr[0]
    for s in directions:
        if (" "+s+" " in newLine):
            info["DIR"]=s[0]
            break
    for s in positions:
        if (" "+s+" " in newLine):
            info["POSITION"]=s
            break
    for s in city_names:
        if (" "+s+" " in newLine):
            info["CITY_NAME"]=s
            break
    for s in str_names:
        if (" "+s+" " in newLine):
            if (info["CITY_NAME"]==s and newLine.count(s)==1 or (s in directions and info["DIR"]==s[0] and newLine.count(s)==1)):
                continue
            info["STR_NAME"]=s
            break
    for s in suff:
        if (" "+s+" " in newLine):
            if (s=="STREET"):
                s=s[:2]
            info["(STR_SUFF)"]=s
            break
    for s in curr:
        if (s.isnumeric() and len(s)==5):
            info["ZIPCODE"]=s
            break
    # print(info)
    # print('\n')
    data.append(info)
    cnt+=1
file.close()
with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/data.txt", "w") as temp:
    for info in data:
        for s in label:
            temp.write(s+": "+info[s]+'\n')
        temp.write("\n")
    temp.close()
