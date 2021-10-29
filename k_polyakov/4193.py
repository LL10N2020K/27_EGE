from itertools import combinations 

with open('27-67b.txt') as f:
    n = int(f.readline())

    k = {0}

    for _ in range(n):
        elems = list(map(int, f.readline().split()))[1:]
        i = 0
        chet = {0}
        while i <= len(elems):
            for el in combinations(elems, r = i):
                if sum(el)%2 == 0:
                    chet.add(sum(el))
            i += 1
        combo = {(x + y) for x in k for y in chet}
        k = {x%5: x for x in sorted(combo)}.values()

    print(max(x for x in k if x%2 == 0 and x%5 != 0))
