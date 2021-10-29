with open('27b (1).txt') as f:
    n = int(f.readline())

    k = {0}
    s = 0

    for i in range(n):
        troyka = list(map(int, f.readline().split()))
        s += min(troyka)
        combinations = {x + y for x in k for y in troyka}
        k = {x%7: x for x in sorted(combinations)}.values()

    print(max(x for x in k if x%7 == s%7))
