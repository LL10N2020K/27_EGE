from itertools import combinations

with open('27-60b.txt') as f:
    n = int(f.readline())

    k = [float('inf')]*25
    razn = {0}
    s = 0

    for i in range(n):
        x = int(f.readline())
        s += x
        k[x%25] = min(k[x%25], x)
        
    j = 0
    while j <= 5:
        for w in combinations(k, r = j):
            razn.add(sum(w))
        j += 1
    print(s) if s%25 == 0 else print(s - min( k[s%25], min(x for x in razn if x%25 == s%25)))
