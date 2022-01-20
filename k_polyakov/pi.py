def variants(t): 
    un = lambda x: x < 0 and (-x)%10 == 8

    with open('27-93a.txt') as f:
        n, k = map(int, f.readline().split())
        cUn, s, m = 0, 0, 0
        D = t
        total = [[] for i in range(D)]
        for j in range(n):
            x = int(f.readline())
            s += x
            if cUn == k and s%D == 0: m = max(m, s)
            cUn += un(x)
            flag = True
            if len(total[s%D]) != 0:
                for prefix in total[s%D]:
                    if cUn - prefix[1] == k:
                        m = max(m, s - prefix[0])
                    if cUn - prefix[1] > k:
                        total[s%D].remove(prefix)
                    if prefix[1] == cUn:
                     flag = False
            if flag:
                total[s%D] += [[s, cUn]]
        print(m)


    f = open('27-93a.txt')
    n, k = map(int, f.readline().split())
    cUn, s, m = 0, 0, 0
    total = []
    for j in range(n):
        x = int(f.readline())
        s += x 
        cUn += un(x)
        if cUn == k and s%D == 0: m = max(m, s)
        if len(total) != 0:
            for prefix in total:
                if cUn - prefix[1] == k and (s - prefix[0])%D == 0:
                    m = max(m, s - prefix[0])
        total += [[s, cUn]]
    print(m, '\n')

for d in range(43, 44):
    variants(d)