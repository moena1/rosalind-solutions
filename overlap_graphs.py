f = open("rosalind_grph.txt", "r")
f = f.readlines()

nameList = []
nucList = []
nuc = ""

for line in f:
    line = line.strip()
    if line[0] == ">":
        if line != ">":
            nameList.append(line)
        if nuc != "":
            nucList.append(nuc)
        nuc = ""
    else:
        nuc += line

for i in range(0, len(nucList)):
    for j in range(0, len(nucList)):
        if i != j:
            if nucList[i][len(nucList[i])-3:len(nucList[i])] == nucList[j][0:3]:
                print(nameList[i].strip(">") + " " + nameList[j].strip(">"))
            
        
        
        

