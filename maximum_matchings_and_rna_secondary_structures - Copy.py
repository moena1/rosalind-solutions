import math

f = open("rosalind_mmch.txt", "r")
f = f.read()
string = f.strip()

c = string.count("C") 
a = string.count("A")
g = string.count("G")
u = string.count("U")

if c > g:
    cg = math.factorial(c)//math.factorial(c-g)
else:
    cg = math.factorial(g)//math.factorial(g-c)

if a > u:
    au = math.factorial(a)//math.factorial(a-u)
else:
    au = math.factorial(u)//math.factorial(u-a)

print(cg*au)

