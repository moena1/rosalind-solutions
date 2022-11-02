f = open("rosalind_splc.txt", "r")
f = f.readlines()

m = 0
introList = []
wholeSeq = ""
intro = ""

for line in f:
    line = line.strip()
    if line[0] == ">":
        m += 1
    if m < 2:
        if line[0] != ">":
            wholeSeq += line
    else:
        if line[0] == ">":
            introList.append(intro)
            intro = ""
        if line[0] != ">":
            intro += line
            
print(wholeSeq)
print(introList)

for k in range(0, len(introList)):
    wholeSeq = wholeSeq.replace(introList[k], "")

rna = ""
for elem in wholeSeq:
    if elem == "T":
        rna += "U"
    else:
        rna += elem

msg = ""

multThree = int(len(rna)/3)
for i in range(1, multThree):
    codon = rna[i*3-3:i*3]
    if codon == "UUU" or codon == "UUC":
        msg += "F"
    if codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
        msg += "L"
    if codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
        msg += "S"
    if codon == "UAU" or codon == "UAC":
        msg += "Y"
    if codon == "UAA" or codon == "UAG" or codon == "UGA":
        break
    if codon == "AUG":
        msg += "M"
    if codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
        msg += "A"
    if codon == "UGU" or codon == "UGC":
        msg += "C"
    if codon == "UGG":
        msg += "W"
    if codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
        msg += "P"
    if codon == "CAU" or codon == "CAC":
        msg += "H"
    if codon == "CAA" or codon == "CAG":
        msg += "Q"
    if codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
        msg += "R"
    if codon == "AUU" or codon == "AUC" or codon == "AUA":
        msg += "I"
    if codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
        msg += "T"
    if codon == "AAU" or codon == "AAC":
        msg += "N"
    if codon == "AAA" or codon == "AAG":
        msg += "K"
    if codon == "AGU" or codon == "AGC":
        msg += "S"
    if codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
        msg += "V"
    if codon == "GAU" or codon == "GAC":
        msg += "D"
    if codon == "GAA" or codon == "GAG":
        msg += "E"
    if codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
        msg += "G"
        
print(msg)
