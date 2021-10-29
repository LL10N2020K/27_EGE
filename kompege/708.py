with open('27-A (6).txt') as f:
    n = int(f.readline())

    k = [0]*(10000 + 1)
    count = 0

    for i in range(n):
        x = int(f.readline())

        j = 0
        while j < x - j:
            count += (k[j] * k[x - j])
            j += 1
            
        if j == x - j:
            count += k[j] * (k[j] - 1)//2
            
        k[x] += 1

    print(count)
