import math
f = open("rosalind_prot.txt", "r")
f = f.read()

f = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

reversedF = f[::-1]
rna2 = ""
for elem in reversedF:
    if elem == "T":
        rna2 += "U"
    else:
        rna2 += elem

###RNA Translation
rna1 = ""
for elem in f:
    if elem == "A":
        rna1 += "U"
    if elem == "T":
        rna1 += "A"
    if elem == "C":
        rna1 += "G"
    if elem == "G":
        rna1 += "C"
rna1 = rna1[::-1]
rna2 = rna2[::-1]

print(rna1)
print(rna2)
msgList = []
msg = ""

for j in range(0, 2):
    if j == 0:
        x = rna1
    elif j == 1:
        x = rna2
    i = 0
    while i < len(f):
        codon = x[i:i+3]
        print(codon)
        if codon == "AUG":
            if msg != "":
                msgList.append(msg)
            msg = ""
            msg += "M"
            i += 3
            codon = x[i:i+3]
            while codon != "UAA" and codon != "UAG" and codon != "UGA" and codon != "AUG":
                if len(codon) == 3:
                    print(codon)
                if codon == "UUU" or codon == "UUC":
                    msg += "F"
                if codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
                    msg += "L"
                if codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
                    msg += "S"
                if codon == "UAU" or codon == "UAC":
                    msg += "Y"
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
                if (i + 3) < len(f):
                    i += 3
                    codon = x[i:i+3]
                else:
                    break
        else:
            i += 1



print(msgList)
    

