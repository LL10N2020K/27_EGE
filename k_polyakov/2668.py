with open('27-8a.txt') as f:
    n = int(f.readline())

    k = [int(f.readline()) for x in range(4)]
    s_min = float('inf')
    two_min = float('inf')
    
    for _ in range(n - 5):
        x = int(f.readline())
        s_min = min(s_min, x**2 + two_min)
        two_min = min(two_min, k[0]**2)
        k.remove(k[0])
        k.append(x)

    print(s_min)

        
    
