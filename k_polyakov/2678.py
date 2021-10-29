with open('27-18b.txt') as f:
    n = int(f.readline())

    k = [int(f.readline()) for i in range(5)]
    count = 0

    for i in range(n):
        x0 = k.pop(0)

        for y in range(len(k)):
            if (x0*k[y])%13 == 0 and (x0+k[y])%2 != 0:
                count += 1
        x1 = f.readline()
        if x1 != '':
            k.append(int(x1))
        
    print(count)
