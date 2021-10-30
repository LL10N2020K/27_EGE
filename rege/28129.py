with open('28129_B.txt') as f:
    n = int(f.readline())

    k = [0]*160
    p1 = 0
    p2 = 0

    for i in range(n):
        x = int(f.readline())

        for y in range(160):
            if x%160 != k[y]:
                if (x*k[y])%7 == 0:
                    if (x*k[y]) > p1*p2:
                        p1 = x
                        p2 = k[y]

        k[x%160] = max(k[x%160], x)

    print(p1, p2)
