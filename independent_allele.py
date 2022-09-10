from math import comb

f = open("rosalind_lia.txt", "r")
f = f.read()
g = f.split(" ")
k = int(g[0])
n = int(g[1])

prob = 0
for i in range(n, 2**k + 1):
    prob += comb(2**k, i)*0.25**i*0.75**(2**k-i)

print(round(prob,3))
