with open('27b (2).txt') as f:
    n = int(f.readline())

    k = {0}

    for i in range(n):
        troyka = list(map(int, f.readline().split()))
        pairs = {troyka[0] + troyka[1], troyka[0] + troyka[2], troyka[1] + troyka[2]}
        combinations = {x + y for x in k for y in pairs}
        k = {x%5: x for x in sorted(combinations)}.values()

    print(max(x for x in k if x%5 != 0))
