import math
f = open("rosalind_iprb.txt", "r")
f = f.read()
g = f.split(" ")
k = int(g[0])
m = int(g[1])
n = int(g[2])

def nCr(number):
    return ((math.factorial(number) / (2 * math.factorial(number-2))))

    
totalComb = nCr(k + m + n)
dComb = nCr(k) + k*n + k*m + 0.75*nCr(m) + 0.5*m*n

print(round((dComb/totalComb), 5))
