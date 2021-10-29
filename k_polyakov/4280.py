with open('27-74b.txt') as f:
    n = int(f.readline())

    k = [[0,0]]
    count = 0

    for i in range(n):
        x = int(f.readline())
        k = [[x + y, l + 1] for y, l in k] + [[x, 1]]
        for j in k:
            if (j[0]%39 == 0) and (j[1] <= 20):
                count += 1
            if j[1] > 20:
                k.remove(j)

    print(count)
                
