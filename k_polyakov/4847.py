un = lambda x: x >= 0 and x%2 == 0

with open('27-92a.txt') as f:
    n = int(f.readline())
    cUn, s, m = 0, 0, 0
    INF = float('inf')
    total = [[INF, INF]]
    for j in range(n):
        x = int(f.readline())
        cUn += un(x)
        s += x
        for prefix in total:
            if cUn - prefix[1] == 1:
                m = max(m, s - prefix[0])
            if cUn - prefix[1] > 2:
                total.remove(prefix)
        total.append([s, cUn])
    print(m)
        
with open('27-92a.txt') as f:
    n = int(f.readline())
    cUn, s, m = 0, 0, 0
    INF = float('inf')
    total = [INF]*n
    for j in range(n):
        x = int(f.readline())
        cUn += un(x)
        s += x
        if total[cUn - 1] != INF:
            m = max(m, s - total[cUn - 1])
        total[cUn] = s 
    print(m)
            
