with open('27-B (21).txt') as f:
    n = int(f.readline())

    k = [0]*3
    r = float('inf')

    for i in range(n):
        k_new = sorted(map(int, f.readline().split()))

        for y in range(3):
            k[y] += k_new[y]
            
        if (k_new[2] - k_new[0])%2:
            r = min(r, k_new[2] - k_new[0])
        if (k_new[2] - k_new[1])%2:
            r = min(r, k_new[2] - k_new[1])

    print(k[2]) if k[2]%2 == 0 else print(k[2] - r)

    
        
