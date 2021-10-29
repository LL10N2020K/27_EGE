with open('27-79b.txt') as f:
    n = int(f.readline())

    one = set()
    two = {}
    dl = 0

    for i in range(n):
        x = int(f.readline())
        if x%21 == 0:
            if x not in one:
                one.add(x)
                two[x] = i - 1
        if x**2 in one:
            dl = max(dl, i - two[x**2])

    print(dl)

    
        
