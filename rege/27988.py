with open('27988_B.txt') as f:
    n = int(f.readline())

    k  = [0]*26
    maxi = float('-inf')

    for i in range(n):
        x = int(f.readline())
        
        for y in range(26):
            if (x*k[y])%26 == 0:
                maxi = max(maxi, x*k[y])

        k[x%26] = max(x, k[x%26])

    print(maxi)
