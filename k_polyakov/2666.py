with open('27-6b.txt') as f:
    n = int(f.readline())

    k2 =  k3 = kmax = 0
    k6 = {0}
    
    for _ in range(n):
        x = int(f.readline())
        kmax = max(x, kmax)
        if x%2 == 0:
            k2 = max(x, k2)
        if x%6 == 0:
            k6.add(x)
        if x%3 == 0:
            k3 = max(x, k3)
    k6 = (sorted([int(x) for x in k6], reverse = 1))[:2:]

    print(max((k3*k2), (k6[0]*kmax), (k6[0]*k6[1])))
        
        
