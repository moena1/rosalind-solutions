f = open("rosalind_hamm.txt", "r")
f = f.readlines()
s = f[0].strip()
t = f[1].strip()

output = ""

stringLength = len(s)
hammingDist = 0

for i in range(0, stringLength):
    if s[i] != t[i]:
        hammingDist += 1
        
print(hammingDist)
