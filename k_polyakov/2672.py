with open('27-12b.txt') as f:
    n = int(f.readline())

    k = [0]*6
    count = 0

    for i in range(n):
        x = int(f.readline())

        for y in range(6):
            if (x*y)%6 == 0:
                count += k[y]
        k[x%6] += 1

    print(count)
