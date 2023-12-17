file_path = "D:/programming/ED/BIC/py/r.txt"

with open(file_path, "r") as f:
    pattern = f.readline().strip()

# pattern = input()

for x in reversed(pattern):
    if x == "A":
        print("T", end="")
    elif x == "T":
        print("A", end="")
    elif x == "C":
        print("G", end="")
    elif x == "G":
        print("C", end="")
