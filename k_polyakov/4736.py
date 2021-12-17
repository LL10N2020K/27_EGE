with open('27-84b.txt') as f:
    n, k = map(int, f.readline().split())
    a = [int(x) for x in f]

    r = [0,0]
    total = {False: False}

    for j in range(n):
        x = a[j]
        if x < 0: print(x)
        combinations = [[x + y, 1 + total[y]] for y in total.keys()]

        for el in combinations:
            s = el[0]
            l = el[1]
            if s <= k and ((s not in total) or (l > total[s])):
                total[s] = l

    for s, l in total.items():
        if (abs(k - s) < abs(k - r[0])) or ((abs(k - s) == abs(k - r[0])) and l > r[1]):
            r[0] = s
            r[1] = l

    print(r[1])
