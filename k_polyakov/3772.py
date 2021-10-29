from itertools import combinations

k = tuple(sorted([int(x) for x in open('27-53b.txt')]))

for x in combinations((k[1:]), 3):
    if sum(x)%3 == 0:
        print(sum(x))
        break

