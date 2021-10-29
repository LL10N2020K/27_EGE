with open('27-7b.txt') as f:
    n = int(f.readline())

    kmax = 0
    k7 = {0}
    
    for _ in range(n):
        x = int(f.readline())
        if x%49 != 0:
            kmax = max(x, kmax)
        if x%7 == 0:
            k7.add(x)
    k7 = (sorted([int(x) for x in k7 if x%49 != 0], reverse = 1))[:2:]

    print(max((kmax*k7[0]), (k7[0]*k7[1])))
        
        
