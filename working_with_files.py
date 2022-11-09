f = open("rosalind_ini5.txt", "r")
f = f.readlines()

x = 0

for elem in f:
    if x % 2 == 1:
        print(elem.strip())
    x += 1
