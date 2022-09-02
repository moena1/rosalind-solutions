import itertools

f = open("rosalind_perm.txt", "r")
f = f.read()

permList = []
for i in range (0, int(f)):
    permList.append(i+1)

total = 1
for i in range(1, int(f) + 1):
    total = total * i
print(total)

x = list(itertools.permutations(permList))
for item in x:
    item = str(item)
    item = item.strip(")")
    item = item.strip("(")
    item = item.replace(",", "")
    print(item)

