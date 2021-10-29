with open('27-B (19).txt') as f:
    n = int(f.readline())

    k = [0]*3
    min_razn = {0}

    for i in range(n):
        k_new = sorted(map(int, f.readline().split()))

        for y in range(3):
            k[y] += k_new[y]
    
        min_razn.add(k_new[2] - k_new[1])

    print(k[2] - min(x for x in filter(lambda x: x!= 0, min_razn)))
