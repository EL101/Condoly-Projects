from pprint import pprint

def readData(file, data):
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/"+file, "r") as temp:
        curr={}
        for line in temp:
            L=line[:-1].split(": ")
            if (len(L)==1):
                data.append(curr)
                # if (len(data)<=30):
                #     print(curr)
                curr={}
            elif (len(L)==2):
                curr[L[0]]=L[1]
        temp.close()
matches=[]
readData("matches.txt", matches)
def matchOriginal(data):
    original=[]
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/CDB29AJ-Condominium-List.TXT", "r") as temp:
        block=[]
        for line in temp:
            curr=line[:-1].split()
            if ((not len(curr)==0) and (curr[0]=='-' or curr[0]=='0')):
                curr.remove(curr[0])
            if (len(curr)==0):
                continue
            if (curr[0].isnumeric() and len(curr[0])==8):
                original.append(block)
                block=[]
            newLine=""
            for s in curr:
                newLine+=" "+s
            block.append(newLine[1:])
        if (len(block)>0):
            original.append(block)
        temp.close()
    # pprint(original)
    finalList=[]
    for info in matches:
        rem=[]
        for block in original:
            found=False
            for line in block:
                if (" "+info["ZIPCODE"] in line and " "+info["STR_NAME"]+" " in line):
                    found=True
                    break
            if (found):
                finalList.append(block)
                finalList[-1].append("UNITS: "+info["UNITS"]+"\n")
                rem=block
                break
        if (rem!=[]):
            original.remove(rem)
    return finalList
def writeOut(data):
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/finalList.txt", "w") as temp:
        for s in data:
            for line in s:
                temp.write(line+"\n")
            temp.write("\n")
writeOut(matchOriginal(matches))
def cleanData():
    info=""
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/finalList.txt", "r") as temp:
        for line in temp:
            if ("OD 40223 C O N D O M I N I U M D I R E C T O R L I S T PAGE" in line or "1 CDB29A S E C R E T A R Y O F S T A T E RUN DATE 6/12/24" in line):
                continue
            else:
                info+=line
        temp.close()
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/finalList.txt", "w") as temp:
        temp.write(info)
cleanData()
def compareData():
    currFinal=[]
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/finalList.txt", "r") as temp:
        block=[]
        for line in temp:
            curr=line[:-1].split()
            if (len(curr)==0):
                continue
            if (curr[0].isnumeric() and len(curr[0])==8):
                currFinal.append(block)
                block=[]
            block.append(line)
        if (len(block)>0):
            currFinal.append(block)
        temp.close()
    prevFinal=[]
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/prevfinalList.txt", "r") as temp:
        block=[]
        for line in temp:
            curr=line[:-1].split()
            if (len(curr)==0):
                continue
            if (curr[0].isnumeric() and len(curr[0])==8):
                prevFinal.append(block)
                block=[]
            block.append(line)
        if (len(block)>0):
            prevFinal.append(block)
        temp.close()
    rem=[]
    for block in prevFinal:
        if (not(block in currFinal)):
            rem.append(block)
    with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/removed.txt", "w") as temp:
        for block in rem:
            for line in block:
                temp.write(line)
            temp.write("\n")
compareData()