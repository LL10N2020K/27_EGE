from itertools import combinations

k = tuple(sorted([int(x) for x in open('27-52a.txt')]))

for x in combinations((k[1:])[::-1], 3):
    if sum(x)%3 == 0:
        print(sum(x))
        break

