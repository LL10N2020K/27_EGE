with open('27-B (12).txt') as f:
    n = int(f.readline())

    k = {0}

    for _ in range(n):
        troyka = list(map(int, f.readline().split()))
        pairs = [troyka[0]+troyka[1], troyka[0]+troyka[2], troyka[1]+troyka[2]]
        combinations = {x + y for x in k for y in pairs}
        k = {x%20: x for x in sorted(combinations)[::-1]}.values()

    print(min(x for x in k if (((x%3 == 0 and x%17 != 0) or (x%3 != 0 and x%17 == 9)))))
