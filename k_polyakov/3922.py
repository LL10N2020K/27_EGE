with open('27-62b.txt') as f:
    n = int(f.readline())
    
    k = sorted(list(map(int, f.readlines())))
    k_saved = {x for x in k}
    count = 0

    for i in range(n - 1):
        
        for j in range(1, 101):
            y = 1
            s = k[i]
            
            while s + j in k_saved:
                s += j
                y += 1
            count = max(count, y)

    print(count)
            
