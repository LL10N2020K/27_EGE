with open('27-B (4).txt') as f:
    n = int(f.readline())

    k = [0]*2
    cur_min = [float('inf')]*2
    count = 0
    
    for i in range(n):
        x = int(f.readline())
        if x%2 == 0:
            if x > cur_min[1]:
                count += k[1]
        elif x%2 != 0:
            if x > cur_min[0]:
                count += k[0]
                
        k[x%2] += 1
        cur_min[x%2] = min(cur_min[x%2], x)

    print(count)

    
