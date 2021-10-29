with open('27b (3).txt') as f:
    n = int(f.readline())

    k = {0}

    for i in range(n):
        pair = list(map(int, f.readline().split()))
        combinations = {x + y for x in k for y in pair}
        k = {x%10: x for x in sorted(combinations)}.values()

    print(max(x for x in k if x%10 != 5))
