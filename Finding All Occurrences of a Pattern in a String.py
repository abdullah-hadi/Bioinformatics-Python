# file_path = "D:/programming/ED/BIC/py/r.txt"

# with open(file_path, "r") as f:
#    pattern = f.readline().strip()
#    genome  = f.readline().strip()

pattern = input()
genome = input()

output = [
    x
    for x in range(len(genome) - len(pattern) + 1)
    if genome[x : x + len(pattern)] == pattern
]

print(len(output))
