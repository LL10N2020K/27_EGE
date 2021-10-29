from math import gcd
from itertools import combinations

def nod(list):
    s = []
    for w in combinations(list, r = 2):
        s.append(gcd(w[0], w[1]))
    return s

with open('27-36b.txt') as f:
    n = int(f.readline())

    k = {0}
    
    for i in range(n):
        troyka = [int(x) for x in f.readline().split()]
        combo = {sum([x, y]) for x in nod(troyka) for y in k}
        k = {x%10: x for x in sorted(combo)}.values()

    print(max(x for x in k if x%10 == 0))
