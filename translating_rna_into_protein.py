import math
f = open("rosalind_prot.txt", "r")
f = f.read()
msg = ""

multThree = int(len(f)/3)
for i in range(1, multThree):
    codon = f[i*3-3:i*3]
    if codon == "UUU" or codon == "UUC":
        msg += "F"
    if codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
        msg += "L"
    if codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
        msg += "S"
    if codon == "UAU" or codon == "UAC":
        msg += "Y"
    if codon == "UAA" or codon == "UAG" or codon == "UGA":
        print("OO")
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
    

