with open('27_B (2).txt') as f:
    n = int(f.readline())

    k = [[0,0]]
    s = dl = 0

    for _ in range(n):
        x = int(f.readline())
        combinations = [[a + x, b + 1] for a, b in k] + [[x, 1]]
        k = {x[0]%89: x for x in sorted(combinations, key = lambda x: x[0])}.values()

        for one, two in k:
            if (one%89 == 0) and ((one > s) or (one == s and two < dl)):
                s = one
                dl = two
    print(dl)
