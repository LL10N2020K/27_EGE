def spec(x):
    if x < 0:
        n = -x
        s = 0
        while n > 0:
            s += n%3
            n //= 3
        return s == 12
    return False

with open('27-91a.txt') as f:
    N, K, D = map(int, f.readline().split())

    INF = 10**30
    T = [[INF]*D for i in range(K)]
    
    special, s, m = 0, 0, 0

    for j in range(N):
        x = int(f.readline())
        s += x
        l = j + 1
        special += spec(x)
        if special%K == 0 and l%D == 0:
            m = max(m, s)
        if T[special%K][l%D] != INF:
            m = max(m, s - T[special%K][l%D])

        T[special%K][l%D] = min(T[special%K][l%D], s)

    print(m)




        



   




        
    
