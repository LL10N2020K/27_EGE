def unusual(y):
    if y < 0:
        y = abs(y)
        return all(y%j != 0 for j in range(2, int(y**0.5) + 1))
    return 0
    

with open('27-88a.txt') as f:
    N, K = map(int, f.readline().split())
    
    tSmall, tBig = [10**10]*K, [10**10]*K
    M, S, cUn = 0, 0, 0
    
    for j in range(N):
        x = int(f.readline())
        S += x
        cUn += unusual(x)
        if S - tSmall[cUn%K] > M and tSmall[cUn%K] != 10**10: M = S - tSmall[cUn%K]
        if S - tBig[cUn%K] > M and tBig[cUn%K] != 10**10: M = S - tBig[cUn%K]
        if S > 0: tBig[cUn%K] = min(tBig[cUn%K], S)
        if S < 0: tSmall[cUn%K] = min(tSmall[cUn%K], S)

    print(M)
        
            
    
