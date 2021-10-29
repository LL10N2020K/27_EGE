from itertools import combinations

with open('27-61b.txt') as f:
    n = int(f.readline())

    k = [float('inf')]*100
    razn = {0}
    s = 0

    for i in range(n):
        x = int(f.readline())
        s += x
        k[x%100] = min(k[x%100], x)
        
    j = 0
    while j <= 3:
        for w in combinations(k, r = j):
            razn.add(sum(w))
        j += 1
        
    print(s) if s%100 == 50 else print(s - min( k[(50 - s%100)%100], min(x for x in razn if (s - x)%100 == 50)))
