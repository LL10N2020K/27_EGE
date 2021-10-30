with open('28133_B.txt') as f:
    n = int(f.readline())

    k = [0]*120
    maxi = [float('-inf')]*2

    for i in range(n):
        x = int(f.readline())

        for y in range(120):
            if (x + y)%120 == 0:
                if (x + k[y]) > sum(maxi):
                    maxi = [k[y], x]

        k[x%120] = max(x, k[x%120])

    print(*maxi)
    
