with open('27-38b.txt') as f:
    n = int(f.readline())

    k = [0]*10
    s = centr = 0

    for i in range(n):
        x = int(f.readline())
        k[x] += 1
        
    for j in range(10):
        if k[j] != 0:
            if k[j]%2 == 0:
                s += k[j]*j
            else:
                s += (k[j] - 1)*j
                centr = max(centr, j)

    print(s + centr)
                
