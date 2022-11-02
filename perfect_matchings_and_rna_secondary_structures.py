import math

f = open("rosalind_pmch.txt", "r")
f = f.read()
string = f.strip()

cg = string.count("G") 
au = string.count("A")

print(math.factorial(cg)*math.factorial(au))



