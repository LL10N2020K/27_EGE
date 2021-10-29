from itertools import combinations as cmb
from functools import reduce
from math import gcd

def nok(set):
    return reduce(lambda x, y: x*y//gcd(x, y), set)

with open('27-77b.txt') as f:
    n = int(f.readline())

    k = {0}

    for i in range(n):
        b = list(map(int, f.readline().split()))[1:]
        combinations = {nok({x, y}) for x, y in cmb (b, 2)}
        s = {sum({x, y}) for x in k for y in combinations}
        k = {x%35: x for x in sorted(s)}.values()

    print(max(x for x in k if (x%5 == 0 or x%7 == 0) and x%35 != 0))
