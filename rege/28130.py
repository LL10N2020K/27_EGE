with open('28130_B.txt') as f:
    n = int(f.readline())

    k = [0]*80
    big_k = [0]*80
    count = 0

    for i in range(n):
        x = int(f.readline())
        
        for y in range(80):
            if x > 50:
                if (x + y)%80 == 0:
                    count += k[y]
            else:
                if (x + y)%80 == 0:
                    count += big_k[y]
        
        if x > 50:
            big_k[x%80] += 1
            
        k[x%80] += 1

    print(count)
    
