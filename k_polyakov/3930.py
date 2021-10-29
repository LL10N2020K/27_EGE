from itertools import combinations

k = tuple(sorted([int(x) for x in open('27-63b.txt')]))

for x in combinations(k[1:], 4):
    if sum(x)%9 != 0:
        print(sum(x))
        break

