import math

f = open("rosalind_prob.txt", "r")
f = f.readlines()
string = f[0].strip()
array = f[1].strip().split(" ")

cg = string.count("G") + string.count("C")
at = string.count("A") + string.count("T")

outputArray = []
for item in array:
    output =  cg * math.log10(float(item)/2) + at * math.log10((1-float(item))/2)
    print(round(output, 3), end=" ")



