f = open("rosalind_tran.txt", "r")
f = f.readlines()

m = 0
seq1 = ""
seq2 = ""

for line in f:
    line = line.strip()
    if line[0] == ">":
        m += 1
    if m < 2:
        if line[0] != ">":
            seq1 += line
    else:
        if line[0] != ">":
            seq2 += line

purines = "AG"
pyrimidines = "CT"
transition = 0
transversion = 0

for i in range (0, len(seq1)):
    if seq1[i] != seq2[i]:
        if seq1[i] in purines and seq2[i] in purines:
            transition += 1
        if seq1[i] in pyrimidines and seq2[i] in pyrimidines:
            transition += 1
        if seq1[i] in purines and seq2[i] in pyrimidines:
            transversion += 1
        if seq1[i] in pyrimidines and seq2[i] in purines:
            transversion += 1
            
print(transition/transversion)

