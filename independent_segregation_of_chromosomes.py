import math

f = open("rosalind_indc.txt", "r")
f = int(f.read())

outputList = []
prob = 0

for i in range(1, f*2 + 1):
    prob += math.factorial(f*2)/math.factorial(i-1)/math.factorial(f*2-i+1)/2 ** (2*f)
    outputList.append(format(round(math.log10(prob), 3), ".3f"))

outputList = outputList[::-1]

for elem in outputList:
    if elem == "-0.000":
        elem = "0.000"
    print(elem, end = " ")
