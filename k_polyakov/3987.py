with open('27-64b.txt') as f:
    n = int(f.readline())

    k = []

    s = s_max = s_min = 0
    for _ in range(n):
        pair = list(map(int, f.readline().split()))
        if pair[0]%2 != 0:
            s += sum(pair)
            s_min += min(pair)
            s_max += max(pair)
            k.append([(max(pair) + min(pair)), max(pair), min(pair)])
            
    k.sort()
    
    j = 0
    while j <= len(k):
        if (s_max - k[j][1])%2 != 0 and (s_min - k[j][2])%2 == 0:
            print(s - k[j][0])
            break
        j += 1
        
