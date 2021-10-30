with open('28128_B.txt') as f:
    n = int(f.readline())

    k  = [0]*3
    maxi = 1

    for i in range(n):
        x = int(f.readline())
        
        for y in range(3):
            if (x + y)%3 == 0:
                if sum([x, k[y]]) > maxi:
                    maxi = sum([x, k[y]])

        k[x%3]  = max(x, k[x%3])

    print(maxi)
