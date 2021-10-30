with open('27-B_2.txt') as f:
    n = int(f.readline())

    k = [0]*14
    maxi = float('-inf')

    for i in range(n):
        x = int(f.readline())

        for y in range(14):
            if (x*k[y])%14 == 0:
                maxi = max(maxi, x*k[y])

        k[x%14] = max(k[x%14], x)

    print(maxi)
        

   
