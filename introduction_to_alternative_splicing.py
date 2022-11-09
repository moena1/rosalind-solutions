import math

f = open("rosalind_aspc.txt", "r")
f = f.read()
f = f.split(" ")

n = int(f[0])
k = int(f[1])

count = 0

for x in range (k, n + 1):
    count = (count + math.factorial(n)//math.factorial(x)//math.factorial(n-x))

print(count % 1000000)
