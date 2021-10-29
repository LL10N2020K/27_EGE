with open('27-B.txt') as f:
    n = int(f.readline())

    k = [0]*26
    count = 0

    for i in range(n):
        x = int(f.readline())

        for y in range(26):
            if (x - y)%13 == 0 and (x*y)%2 == 0:
                count += k[y]

        k[x%26] += 1

    print(count)

