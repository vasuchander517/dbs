data = [1, 3, 5]

pairs = []

k = 2

for x in range(len(data)):
    pairs.append((data[x], data[x + 1]))
    if x + 1 == k:
        break

print(pairs)
