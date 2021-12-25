def spec(x):
    s = 0
    while x > 0:
        s += x%3
        x //= 3
    return s == 12

with open('27-90b.txt') as f:
    N, K, D = map(int, f.readline().split())

    T = [[0]*D]*K
    Tall = [0]*K
    s, m = 0, 0
    special = 0

    for j in range(N):
        x = int(f.readline())
        s += x
        special += spec(x)
        l = j + 1
        if special%K == 0 and l%D == 0:
            m = max(m, s)
        if T[special%K][l%D] != 0:
            m = max(m, s - T[special%K][l%D])
        if l%D == 0:
            m = max(m, s - Tall[special%K])
        T[special%K][l%D] = min(T[special%K][l%D], s)
        Tall[special%K] = min(Tall[special%K], s)
        
    print(m)




        



   




        
    
