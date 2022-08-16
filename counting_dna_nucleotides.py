f = open("rosalind_dna.txt", "r")
f = f.read()
a = str(f.count("A"))
c = str(f.count("C"))
g = str(f.count("G"))
t = str(f.count("T"))

print(a + " " + c + " " + g + " " + t)
