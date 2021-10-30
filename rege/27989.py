with open('27989_B.txt') as f:
    n = int(f.readline())

    k  = [0]*26
    count = 0

    for i in range(n):
        x = int(f.readline())
        
        for y in range(26):
            if (x*y)%26 == 0:
                count += k[y]

        k[x%26] += 1

    print(count)
