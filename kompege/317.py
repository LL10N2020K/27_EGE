with open('27-B (2).txt') as f:
    n = int(f.readline())

    k = [0]*34
    count = 0

    for i in range(n):
        x = int(f.readline())

        for y in range(34):
            if (x < y) and ((x + y) <= 34):
                count += k[y]

        if x <= 33:
            k[x] += 1

    print(count)
