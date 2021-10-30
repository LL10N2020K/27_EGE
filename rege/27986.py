with open('27986_B.txt') as f:

    k  = [0]*49
    maxi = float('-inf')

    while True:
        x = int(f.readline())
        if x == 0: break

        for y in range(49):
            if (x*k[y])%7 == 0 and  (x*k[y])%49 != 0:
                maxi = max(maxi, x*k[y])

        k[x%7] = max(x, k[x%7])

    print(maxi)
