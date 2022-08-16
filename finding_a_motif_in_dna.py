f = open("rosalind_subs.txt", "r")
f = f.readlines()
s = f[0].strip()
t = f[1].strip()

output = ""

lenS = len(s)
lenT = len(t)

for i in range(0, lenS - lenT):
    if s[i: i + lenT] == t:
        output += str(i + 1)
        output += " "
        
print(output)
