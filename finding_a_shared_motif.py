f = open("rosalind_lcsm.txt", "r")
f = f.readlines()

nucList = []

addLine = ""
for line in f:
    line = line.strip()
    if line[0] != ">":
        addLine += line
    if line[0] == ">":
        nucList.append(addLine)
        addLine = ""

longest = 0
string = ""
first = nucList[1]

for k in range(0, len(first)):
    good = True
    for j in range(k, len(first)):
        for i in range(1, len(nucList)):
            if good == True:
                if first[k:j] in nucList[i]:
                    pass
                elif first[k:j] not in nucList[i]:
                    good = False
                if i == (len(nucList) - 1):
                    length = j-k
                    if length > longest:
                        longest = length
                        string = first[k:j]
print(string)                


    
    
        
            
        
        

