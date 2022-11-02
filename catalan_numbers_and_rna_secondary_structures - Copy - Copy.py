import math

f = open("rosalind_cat.txt", "r")
f = f.read()
string = f.strip()

cg = string.count("C") 
au = string.count("A")

cg = math.factorial(2*cg)//math.factorial(cg+1)//math.factorial(cg)
au = math.factorial(2*au)//math.factorial(au+1)//math.factorial(au)


print(cg*au)

