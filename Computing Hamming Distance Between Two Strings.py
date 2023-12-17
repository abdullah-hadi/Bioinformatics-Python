file_path = "D:/programming/ED/BIC/py/r.txt"

with open(file_path, "r") as file:
    s1 = file.readline()
    s2 = file.readline()


n = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        n += 1

print(n)
