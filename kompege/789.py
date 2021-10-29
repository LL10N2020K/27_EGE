with open('27-B (18).txt') as f:
    n = int(f.readline())

    k = [0]*2
    k1 = [0]*3

    for i in range(n):
        x = int(f.readline())
        if x == 1:
            k[k1[1]] += k1[0]
            k1[0] = 0
            k1[1] = 1 - k1[1]%2
        else:
            if x%2 == 0:
                k1[2] += k[k1[1]]
                k1[0] += 1
                
    print(k1[2])
                
