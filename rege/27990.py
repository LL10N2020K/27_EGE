with open('27990_B.txt') as f:
    n = int(f.readline())

    k  = [0]*62
    count = 0

    for i in range(n):
        x = int(f.readline())
        
        for y in range(62):
            if (x*y)%62 == 0:
                count += k[y]

        k[x%62] += 1

    print(count)
