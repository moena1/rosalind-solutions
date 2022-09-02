f = open("rosalind_cons.txt", "r")
f = f.readlines()

aList = []
cList = []
gList = []
tList = []

stringList = []
string = ""

for line in f:
    line = line.strip()
    if line[0] == ">":
        if string != "":
            stringList.append(string)
        string = ""
    else:
        string += line
stringList.append(string)

lenFirst = len(stringList[0])
for i in range (0, lenFirst):
    aCount = 0
    cCount = 0
    gCount = 0
    tCount = 0
    for item in stringList:
        if item[i] == "A":
            aCount += 1
        if item[i] == "C":
            cCount += 1
        if item[i] == "G":
            gCount += 1
        if item[i] == "T":
            tCount += 1
    aList.append(aCount)
    cList.append(cCount)
    gList.append(gCount)
    tList.append(tCount)

printString = ""
for j in range(0, lenFirst):
    if max(aList[j], cList[j], gList[j], tList[j]) == aList[j]:
        printString += "A"
    elif max(aList[j], cList[j], gList[j], tList[j]) == cList[j]:
        printString += "C"
    elif max(aList[j], cList[j], gList[j], tList[j]) == gList[j]:
        printString += "G"
    elif max(aList[j], cList[j], gList[j], tList[j]) == tList[j]:
        printString += "T"

print(printString)
print("A:", end= ' ')
for item in aList:
    print(item, end= ' ')
print()
print("C:", end= ' ')
for item in cList:
    print(item, end= ' ')
print()
print("G:", end= ' ')
for item in gList:
    print(item, end= ' ')
print()
print("T:", end= ' ')
for item in tList:
    print(item, end= ' ')
    
