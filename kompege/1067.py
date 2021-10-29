with open('27-B (20).txt') as f:
    n = int(f.readline())

    k = [[0, 0], [0, 0]]
    r = [float('inf')]

    for i in range(n):
        k_new = sorted(map(int, f.readline().split()))
        k[0][0] += k_new[1]
        k[1][0] += k_new[0]
        if k_new[1]%2 == 0:
            k[0][1] += 1
        if k_new[0]%2 == 0:
            k[1][1] += 1
            if k_new[1]%2:
                r += [(k_new[1] - k_new[0])]

    for j in range((k[0][1] + k[1][1])//2 - k[0][1]):
        k[0][0] -= sorted(r)[j] if sorted(r)[j] != 0 else 0
    
    print(k[0][0])
