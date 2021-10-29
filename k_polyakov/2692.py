with open('27-32b.txt') as f:
    n = int(f.readline())

    k = {0}

    for _ in range(n):
        troyka = list(map(int, f.readline().split()))
        combinations = {x + y  for x in k for y in troyka}
        k = {x%11: x for x in sorted(combinations)[::-1]}.values()

    print(min(x for x in k if x%11 == 0))
