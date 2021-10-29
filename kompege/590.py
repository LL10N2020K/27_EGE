with open('27-B (6).txt') as f:
    n = int(f.readline())

    k = [0]*101
    count = 0

    for i in range(n):
        x = int(f.readline())

        for y in range(101):
            if (x > y) and ((x + y) > 50):
                count += k[y]

        k[x] += 1

    print(count)
