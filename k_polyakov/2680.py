with open('27-20b.txt') as f:
    next(f)

    k = {}
    count = 0

    for el in map(lambda x: tuple(map(int, x.split())), f.readlines()):
        k_new = {}
        if el[0] in k:
            k_new[el[1]] = k[el[0]] + 1
        else:
            k_new[el[1]] = 1
        if el[1] in k:
            k_new[el[0]] = k[el[1]] + 1
        else:
            k_new[el[0]] = 1
        k = k_new
        count = max(count, max(k.values()))

    print(count)

    
