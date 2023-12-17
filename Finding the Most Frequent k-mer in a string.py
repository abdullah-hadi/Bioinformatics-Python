# file_path = "D:/programming/ED/BIC/py/r.txt"

# with open(file_path, "r") as f:
#     text = f.readline().strip()
#     k = int(f.readline().strip())

text = input()
k = int(input())

kmers = {}

for x in range(len(text) - k + 1):
    pattern = text[x : x + k]
    kmers[pattern] = kmers.get(pattern, 0) + 1


max = max(kmers.values())
most_frequent_kmers = [key for key, value in kmers.items() if value == max]

print(*most_frequent_kmers)

for value in most_frequent_kmers:
    index = None
    for x in range(len(text) - k + 1):
        if text[x : x + k] == value:
            index = x + 1

    if index is not None:
        print(f"{value} {index+1}")
