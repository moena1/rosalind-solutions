f = open("rosalind_ini3.txt", "r")
f = f.readlines()

string = f[0].strip()
i = f[1].split(" ")

print(string[int(i[0]):int(i[1]) + 1] + " " + string[int(i[2]):int(i[3]) + 1])

