# file_path = "D:/programming/ED/BIC/py/r.txt"
# with open(file_path, "r") as file:
#     s = "".join(file.readlines())


s = input()


skew = [0]
n = 0
for i in range(len(s)):
    if s[i] == "C":
        n -= 1
    if s[i] == "G":
        n += 1
    skew.append(n)

min = min(skew)
indexes = [value for index, value in enumerate(skew) if value == min]

print(*indexes)
