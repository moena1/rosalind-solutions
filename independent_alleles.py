f = open("rosalind_fib.txt", "r")
f = f.read()
g = f.split(" ")
n = int(g[0])
k = int(g[1])

big = 0
little = 1

for i in range (1, n):
    tempBig = big
    tempBig += little
    little = big * k
    big = tempBig

print(little + big)
