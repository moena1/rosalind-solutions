f = open("rosalind_sset.txt", "r")
f = int(f.read().strip())

output = (2 ** f) % 1000000
print(output)
