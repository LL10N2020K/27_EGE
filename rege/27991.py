with open('27991_B.txt') as f:
    n = int(f.readline())

    k  = [0]*34
    maxi = [0]*2

    for i in range(n):
        x = int(f.readline())
        
        for y in range(34):
            if (x*y)%17 == 0 and (x - y)%2 == 0:
                if sum([x, k[y]]) > sum(maxi):
                    maxi = [k[y], x]

        k[x%34]  = max(x, k[x%34])

    print(*maxi)
