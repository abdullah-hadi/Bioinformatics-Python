# file_path = "D:/programming/ED/BIC/py/r.txt"

# with open(file_path, "r") as f:
#     text = f.readline().strip()
#     pattern = f.readline().strip()

text = input()
pattern = input()


count = 0
for x in range(len(text) - len(pattern) + 1):
    if text[x : x + len(pattern)] == pattern:
        count += 1

print(count)
