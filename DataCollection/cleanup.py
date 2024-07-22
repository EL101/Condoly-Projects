data=[]
with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/finalListExcel.csv", "r") as temp:
    for line in temp:
        if ("INVOLUNTARY DISSOLUTION" in line):
            continue
        # curr=line[:-1].split(',')
        # found=False
        # # print(curr)
        # for i in curr:
        #     if (i==''):
        #         found=True
        #         break
        # if (found):
        #     continue
        data.append(line)
    temp.close()

with open("C:/Users/yhk13/OneDrive/Documents/Condoly/DataCollection/finalListExcel.csv", "w") as temp:
    for i in data:
        temp.write(i)
    temp.close()