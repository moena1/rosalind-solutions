f = open("rosalind_pdst.txt", "r")
f = f.readlines()

seq = ""
seqList = []

for line in f:
    line = line.strip()
    if line[0] == ">":
        if seq != "":
            seqList.append(seq)
        seq = ""
    else:
        seq += line

for item in seqList:
    for elem in seqList:
        count = 0
        for i in range(0, len(elem)):
            if item[i] != elem[i]:
                count += 1
        print(format(round(count/len(elem), 5), ".5f"), end = " ")
    print()
            

        
