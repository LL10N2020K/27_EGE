with open('27_B (1).txt') as f:
    n = int(f.readline())

    k = [[0, 0]]
    s = [0, 0]

    for i in range(n):
        x = int(f.readline())
        combinations = [[y + x, z + 1] for y, z in k] + [[x, 1]]
        k = {x[0]%89: x for x in sorted(combinations)}.values()

        for y, z in k:
            if y%89 == 0:
                if y > s[0] or (y == s[0] and z < s[1]):
                    s[0] = y
                    s[1] = z

    print(s[1])

