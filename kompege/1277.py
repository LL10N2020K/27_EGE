with open('27_B (4).txt') as f:
    n = int(f.readline())

    k = {0}

    for i in range(n):
        troyka = list(map(int, f.readline().split()))
        combinations = {x + y for x in k for y in troyka}
        k = {x%117: x for x in sorted(combinations)[::-1]}.values()

    print(min(x for x in k if x%117 != 11))
