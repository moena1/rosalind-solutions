f = open("rosalind_ini2.txt", "r")
f = f.read()
fList = f.split(" ")

answer = int(fList[0]) ** 2 + int(fList[1]) ** 2
print(answer)

