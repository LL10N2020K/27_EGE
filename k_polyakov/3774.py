from itertools import combinations

k = tuple(sorted([int(x) for x in open('27-55b.txt')]))[1:50]

min_s = float('inf')
for x in combinations((k), 4):
    if sum(x)%4 == 0 and sum(x) < min_s:
        min_s = sum(x)

print(min_s)

