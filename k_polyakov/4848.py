un = lambda x: x < 0 and (-x)%10 == 3

with open('27-93b.txt') as f:
    n, k = map(int, f.readline().split())
    cUn, s, m = 0, 0, 0
    INF = float('inf')
    total = []
    for j in range(n):
        x = int(f.readline())
        cUn += un(x)
        s += x
        for prefix in total:
            if cUn - prefix[1] == k:
                m = max(m, s - prefix[0])
            if cUn - prefix[1] > k:
                total.remove(prefix)
        total.append([s, cUn])
    print(m)

#НЕБОЛЬШАЯ ПРАВКА (НЕ БЫЛ ОБРАБОТАН ИСКЛЮЧИТЕЛЬНЫЙ СЛУЧАЙ)

un = lambda x: x < 0 and (-x)%10 == 3

with open('27-93b.txt') as f:
    n, k = map(int, f.readline().split())
    cUn, s, m = 0, 0, 0
    INF = float('inf')
    total = []
    for j in range(n):
        x = int(f.readline())
        s += x
        if cUn == k: m = max(m, s)
        cUn += un(x)
        for prefix in total:
            if cUn - prefix[1] == k:
                m = max(m, s - prefix[0])
            if cUn - prefix[1] > k:
                total.remove(prefix)
        total.append([s, cUn])
    print(m)
