f = open("rosalind_sseq.txt", "r")
f = f.readlines()

m = 0
wholeSeq = ""
subSeq = ""
output = ""

for line in f:
    line = line.strip()
    if line[0] == ">":
        m += 1
    if m < 2:
        if line[0] != ">":
            wholeSeq += line
    else:
        if line[0] != ">":
            subSeq += line
            
subIndex = 0

for i in range (0, len(wholeSeq)):
    if subIndex != len(subSeq):
        if wholeSeq[i] == subSeq[subIndex]:
            output = output + str(i + 1) + " "
            subIndex += 1

print(output)

