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
    print(kmers)  # for printing every value in loop (dictionary )


max = max(kmers.values())
most_frequent_kmers = [key for key, value in kmers.items() if value == max]

print(*most_frequent_kmers)

print("end of most freq")


for pattern in most_frequent_kmers:
    for x in reversed(pattern):
        if x == "A":
            print("T", end="")
        elif x == "T":
            print("A", end="")
        elif x == "C":
            print("G", end="")
        elif x == "G":
            print("C", end="")
    print(end=" ")
