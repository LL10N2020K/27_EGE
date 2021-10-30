with open('27-B.txt') as f:
    n = int(f.readline())

    k = [0]*3
    r = {0}

    for i in range(n):
        k_new = sorted(map(int, f.readline().split()))

        for y in range(3):
            k[y] += k_new[y]

        if k_new[2]%2 != k_new[1]%2:
            r.add(k_new[2] - k_new[1])

    print(k[0]) if k[1]%2 != k[2]%2 else print(k[0] + min([x for x in r if x != 0]))
