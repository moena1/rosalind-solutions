import math
f = open("rosalind_gc.txt", "r")
f = f.readlines()
highestgcContent = ""
highestgcValue = 0
gcVal = 0

for line in f:
    if line[0] == ">":
        if gcVal > highestgcValue:
            highestgcValue = gcVal
            highestgcContent = gcContent
        gcContent = line
        seq = ""
    else:
        seq += line
        gc = seq.count("G") + seq.count("C")
        at = seq.count("A") + seq.count("T")
        gcVal = gc/(gc + at)

if gcVal > highestgcValue:
    highestgcValue = gcVal
    highestgcContent = gcContent

print(highestgcContent.strip(">"))
print(round(highestgcValue*100, 6))
