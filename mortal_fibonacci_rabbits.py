f = open("rosalind_fibd.txt", "r")
f = f.read()
g = f.split(" ")
n = int(g[0])
m = int(g[1])

pairCount = [None] * (n +1)
pairCount[0] = 0
pairCount[1] = 1

def fibonacci(i):
    if pairCount[i] != None:
        return pairCount[i]
    else:
        pairCount[i] = fibonacci(i - 2) + fibonacci(i - 1)
        return pairCount[i]

def rab(j):
    if pairCount[j] != None:
        return pairCount[j]
    else:
        toAdd = 0
        for k in range(0, m - 1):
            toAdd += rab(j - m + k)
        pairCount[j] = toAdd
        return pairCount[j]

fibonacci(m)
print(rab(n))



