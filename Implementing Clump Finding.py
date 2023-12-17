file_path = "D:/programming/ED/BIC/py/r.txt"

with open(file_path, "r") as f:
    genome = f.readline().strip()
    k, L, t = map(int, f.readline().strip().split())


genome = input()
k, L, t = map(int, input().strip().split())

window = len(genome) - L + 1
combinations = L - k + 1

final = set()
for x in range(window):
    
    clumps = {}

    for y in range(x, x + L + 1 - k):

        pattern = genome[y : y + k]
        clumps[pattern] = clumps.get(pattern, 0) + 1

    final.update(key for key, value in clumps.items() if value >= t)

print(*final)
