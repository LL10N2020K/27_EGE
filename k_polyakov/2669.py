with open('27-9b.txt') as f:
    n = int(f.readline())

    k = [int(f.readline()) for x in range(6)]
    s_min = float('inf')
    
    for _ in range(n - 6):
        x = int(f.readline())
        if x%2 != 0:
            m = min([x for x in k if x%2 != 0], default = float('inf'))
            s_min = min(s_min, x*m)
        k.append(x)
        k.remove(max(k[0], k[1]))

    print(s_min)

        
    
