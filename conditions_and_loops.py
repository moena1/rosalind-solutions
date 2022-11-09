f = open("rosalind_ini4.txt", "r")
f = f.read()

numList = f.strip().split(" ")
a = numList[0]
b = numList[1]

sum = 0
for x in range(int(a), int(b)+1):
    if x % 2 == 1:
        sum += x

print(sum)
