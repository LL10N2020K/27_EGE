with open('27-58b.txt') as f:
    n = int(f.readline())

    k = [0]*3

    for i in range(n):
        x = int(f.readline())
        k_new = [0]*3
        
        for y in range(3):
            k_new[(x+y)%3] += k[y]
        k_new[x%3] += 1

        for y in range(3):
            k[y] += k_new[y]

    print(k[0])
