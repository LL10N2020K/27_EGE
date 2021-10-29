with open('27-78b.txt') as f:
    n = int(f.readline())
    
    pref_s = [[float('inf')]*37 for i in range(73)]
    pref_l = [[float('inf')]*37 for i in range(73)]
    maxi = l = s = 0

    for i in range(n):
        x = int(f.readline())
        s += x
        mxs, mxl = pref_s[(73 - x)%73][s%37], pref_l[(73 - x)%73][s%37]
        if mxs != float('inf'):
            if s - mxs > maxi or (s - mxs == maxi and i - mxl < l):
                maxi = s - mxs
                l = i - mxl
        if pref_s[x%73][(s - x)%37] == float('inf'):
            pref_s[x%73][(s - x)%37] = s - x
            pref_l[x%73][(s - x)%37] = i - 1

    print(l)
            
