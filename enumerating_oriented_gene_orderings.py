import itertools

f = open("rosalind_perm.txt", "r")
f = f.read()

f = 2

permList = []
for i in range (0, int(f)):
    permList.append(i+1)

total = 1
for i in range(1, int(f) + 1):
    total = total * i
total = total * 2 ** f
print(total)

x = list(itertools.permutations(permList))
for item in x:
    item = str(item)
    item = item.strip(")")
    item = item.strip("(")
    itemList = item.split(",")
    for item in itemList:
        for i in range(0, 2):
            if i == 0:
                print(-1 * int(item), end=' ')
            else:
                print(int(item))
                    

