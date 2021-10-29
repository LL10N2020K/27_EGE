with open('27-54b.txt') as f:
    n = int(f.readline())

    k = [0]*4
    k2 = [0]*4
    k3 = [0]*4
    maxi = 0
    
    for _ in range(n):
        x = int(f.readline())

        for y in range(4):
            if (x+y)%4 == 0: 
                maxi = max(maxi, x+k3[y])

        for y in range(4):
            k3[(x+y)%4] = max(k3[(x+y)%4], x+k2[y])

        for y in range(4):
            k2[(x+y)%4] = max(k2[(x+y)%4], x+k[y])

        k[x%4] = max(k[x%4], x)

    print(maxi)

        
