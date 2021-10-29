with open('27-59b.txt') as f:
    n = int(f.readline())

    k = [0]*10

    for i in range(n):
        x = int(f.readline())
        k_new = [0]*10
        
        for y in range(10):
            k_new[(x+y)%10] += k[y]
        k_new[x%10] += 1

        for y in range(10):
            k[y] += k_new[y]

    print(k[5])
