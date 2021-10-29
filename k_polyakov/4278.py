with open('27-72a.txt') as f:
    n = int(f.readline())

    k = [0]*71
    count = s = 0

    for _ in range(n):
        x = int(f.readline())
        s += x
        if s%71 == 0:
            count += 1
            
        count += k[s%71]
        k[s%71] += 1

    print(count)
        
