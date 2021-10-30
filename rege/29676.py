with open('inf_22_10_20_27b.txt') as f:
    n = int(f.readline())

    k = {0}

    for i in range(n):
        pair = list(map(int, f.readline().split()))
        combinations = {x + y for x in k for y in pair}
        k = {x%3: x for x in sorted(combinations)[::-1]}.values()

    print(min(x for x in k if x%3 == 0))
