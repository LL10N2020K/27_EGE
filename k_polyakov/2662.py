with open('27-2b.txt') as f:
    n = int(f.readline())

    k = [float('inf')]*3
    s = 0
    
    for _ in range(n):
        x, y = list(map(int, f.readline().split()))
        s += max(x, y)
        r = abs(x - y)
        k[r%3] = min(k[r%3], r)

    print(s) if s%3 == 0 else print(s - min({x for x in k if s%3 == x%3}))
