with open('27-19b.txt') as f:
    n = int(f.readline())

    count = mini = maxi = 0
    
    for i in range(n):
        x = int(f.readline())
        cur_min = min(mini*x, maxi*x, x)
        maxi = max(mini*x, maxi*x, x)
        mini = cur_min
        count = max(count, maxi)

    print(count)
