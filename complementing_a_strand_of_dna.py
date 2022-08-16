f = open("rosalind_revc.txt", "r")
f = f.read()
reversedString = f[::-1]
finalString = ""
for char in reversedString:
    if char == "A":
        finalString += "T"
    if char == "T":
        finalString += "A"
    if char == "G":
        finalString += "C"
    if char == "C":
        finalString += "G"

print(finalString)
