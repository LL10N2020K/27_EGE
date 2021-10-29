with open('27-13b.txt') as f:
    n = int(f.readline())

    k = [int(f.readline()) for i in range(7)]
    count = k2 = k7 = k14 = k_not = 0

    for i in range(n - 7):
        x = k[0]
        if x%14 == 0:
            k14 += 1
        elif x%7 == 0:
            k7 += 1
        elif x%2 == 0:
            k2 += 1
        else:
            k_not += 1
        y = int(f.readline())
        if y%14 == 0:
            count += k_not
        if y%7 == 0:
            count += k2
        if y%2 == 0:
            count += k7
        k.remove(k[0])
        k.append(y)
        count += k14

    print(count)
