f = open("rosalind_mrna.txt", "r")
f = f.read()
totalNum = 3

for char in f:
    if char in "FYCHQNKDE":
        totalNum = (totalNum * 2) % 1000000
    if char in "LSR":
        totalNum = (totalNum * 6) % 1000000
    if char in "PTVAG":
        totalNum = (totalNum * 4) % 1000000
    if char == "I":
        totalNum = (totalNum * 3) % 1000000

print(totalNum)
