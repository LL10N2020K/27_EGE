with open('27-56b.txt') as f:
    n = int(f.readline())

    k = [0]*6
    k2 = [0]*6
    k3 = [0]*6
    maxi = 0
    
    for _ in range(n):
        x = int(f.readline())

        for y in range(6):
            if (x+y)%6 == 0: maxi = max(maxi, x+k3[y])

        for y in range(6):
            k3[(x+y)%6] = max(k3[(x+y)%6], x+k2[y])

        for y in range(6):
            k2[(x+y)%6] = max(k2[(x+y)%6], x+k[y])

        k[x%6] = max(k[x%6], x)

    print(maxi)

        
