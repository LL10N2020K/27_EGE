with open('27-73b.txt') as f:
    n = int(f.readline())

    k = [float('inf')]*93
    mxs = s = 0
    
    for _ in range(n):
        x = int(f.readline())
        s += x
        if s%93 == 0:
            mxs = max(mxs, s)
        else:
            if k[s%93] != float('inf'):
                if (s - k[s%93])%2 != 0:
                    mxs = max(mxs, s - k[s%93])
        k[s%93] = min(k[s%93], s)

    print(mxs)
        
