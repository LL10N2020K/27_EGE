with open('27-41b.txt') as f:
    next(f)

    s1 = s2 = s3 = 0
    k = []

    for el in f:
        a = sorted(list(map(int, el.split())))
        s3 += a[0]
        s2 += a[1]
        s1 += a[2]
        if a[1]%2 != a[0]%2:
            k.append([(a[1] - a[0]), a[0], a[1]])
        if a[2]%2 != a[0]%2:
            k.append([(a[2] - a[0]), a[0], a[2]])
        if a[2]%2 != a[1]%2:
            k.append([(a[2] - a[1]), a[1], a[2]])
    k.sort()

    n = 0
    while True:
         if (s1 - k[n][1])%2 == 0 and (s2 - k[n][2])%2 != 0:
            print(s3 + k[n][0])
            break
         n += 1

            
