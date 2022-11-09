f = open("rosalind_inod.txt", "r")
f = f.readlines()

n = f[0]

n = 5
seqList = ["5", "1", "4", "2", "3"]

incList = []
dec = ""

for i in range(0, len(seqList)):
    if seqList[i] == "1":
        incList.append(seqList[i])
        count = 0
    else:
        if len(incList) != 0:
            if seqList[i] > incList[count]:
                incList.append(seqList[i])
                count += 1

print(incList)
