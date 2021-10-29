with open('27-B (3).txt') as f:
    n = int(f.readline())

    yes = [0]*2
    no = [0]*2
    count = 0

    for i in range(n):
        x = int(f.readline())
        if x == 0:
            yes[0] += no[0]
            yes[1] += no[1]
            no = [0]*2
        else:
             no[x%2] += 1
             count += yes[x%2]

    print(count)
