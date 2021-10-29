with open('27-17b.txt') as f:
    n = int(f.readline())

    count = k_not = k2 = k13 = k26 = 0
    k = [int(f.readline()) for i in range(5)]

    for i in range(n - 5):
        x = k.pop(0)
        if x%26 == 0:
            k26 += 1
        elif x%13 == 0:
            k13 += 1
        elif x%2 == 0:
            k2 += 1
        else:
            k_not += 1
        y = int(f.readline())
        if y%26 == 0:
            count += sum([k13, k_not])
        elif y%13 == 0:
            count += sum([k26, k2])
        elif y%2 == 0:
            count += k13
        else:
            count += k26
        k.append(y)

    print(count)
