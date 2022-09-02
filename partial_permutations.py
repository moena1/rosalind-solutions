f = open("rosalind_pper.txt", "r")
f = f.read()
f = f.split(" ")
n = int(f[0])
k = int(f[1])

output = 1
for i in range(0, k):
    output = (output * (n-i)) % 1000000
print(output)

