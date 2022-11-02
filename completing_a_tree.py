f = open("rosalind_seto.txt", "r")
f = f.readlines()

n = f[0]
partOne = f[1].replace("{", "")
partOne = partOne.replace("}", "").strip()
partTwo = f[2].replace("{", "")
partTwo = partTwo.replace("}", "").strip()
setOne = partOne.split(", ")
setTwo = partTwo.split(", ")

listOne = []
listTwo = []
listThree = []
listFour = []
listFive = []
listSix = []

for item in setOne:
    listOne.append(item)
for item in setTwo:
    if item not in listOne:
        listOne.append(item)

for item in setOne:
    if item in setTwo:
        listTwo.append(item)

for item in setOne:
    if item not in setTwo:
        listThree.append(item)

for item in setTwo:
    if item not in setOne:
        listFour.append(item)

for x in range(1, int(n) + 1):
    if str(x) not in setOne:
        listFive.append(str(x))

    if str(x) not in setTwo:
        listSix.append(str(x))

g = open("OOOOOOUUUUUUUUUUUUUUUUUUUUUTPUT.txt", "w")
print("OK")

output = "{"
for elem in listOne:
    output += elem
    output += ", "
output += "}"
g.write(output)

output = "{"
for elem in listTwo:
    output += elem
    output += ", "
output += "}"
g.write(output)

output = "{"
for elem in listThree:
    output += elem
    output += ", "
output += "}"
g.write(output)

output = "{"
for elem in listFour:
    output += elem
    output += ", "
output += "}"
g.write(output)

output = "{"
for elem in listFive:
    output += elem
    output += ", "
output += "}"
g.write(output)

output = "{"
for elem in listSix:
    output += elem
    output += ", "
output += "}"
g.write(output)
