with open('28131_B.txt') as f:
    n = int(f.readline())

    k = [0]*120
    maxi = [float('-inf')]*2

    for i in range(n):
        x = int(f.readline())
        if k[(120 - x%120)%120] > x:
            if sum(maxi) < (x + k[(120 - x%120)%120]):
                maxi = [k[(120 - x%120)%120], x]

        k[x%120] = max(x, k[x%120])

    print(*maxi)
    
