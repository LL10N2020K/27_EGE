with open('27-B (1).txt') as f:
    n = int(f.readline())

    k = [int(x) for x in range(8)]
    p_max = 0

    for i in range(n):
        x = int(f.readline())
        p_max = max(p_max, x*k[0])
        k.append(x)
        k.remove(min(k[0], k[1]))

    print(p_max)
