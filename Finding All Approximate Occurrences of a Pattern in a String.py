file_path = "D:/programming/ED/BIC/py/r.txt"

with open(file_path, "r") as file:
    pattern = file.readline().strip()
    text = file.readline().strip()
    d = int(file.readline().strip())



for i in range(len(text) - len(pattern) + 1):
    
    n = 0
    for x in range(len(pattern)):

        if pattern[x] != text[x + i]:
            n += 1
    if n <= d:
        print(i, end=" ")


