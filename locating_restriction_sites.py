f = open("rosalind_revp.txt", "r")
f = f.readlines()

t = ""
for line in f:
    if line[0] != ">":
        t += line.strip()
print(t)
        
acceptableList = ["TA", "AT", "CG", "GC"]

strLen = len(t)
for i in range(0, strLen):
    for j in range(1, 6):
        x = i
        y = i + (j*2 + 1)
        if y < strLen:
            while x < y:
                if (t[x] + t[y]) in acceptableList:
                    x += 1
                    y -= 1
                else:
                    break
            if (x >= y):
                print(i + 1, len(t[i: i + 2*j +2]))
            
        
                
        
