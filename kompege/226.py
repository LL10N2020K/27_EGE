with open('27-B.txt') as f:
    n = int(f.readline())

    k = [0]*10
    count = 0

    for i in range(n):
        x = int(f.readline())

        for y in range(10):
            if (x + y)%10 == 0:
                count += k[y]

        k[x%10] += 1

    print(count)
