with open('27-B (11).txt') as f:
    n = int(f.readline())

    k = {0}

    for _ in range(n):
        troyka = list(map(int, f.readline().split()))
        pairs = [troyka[0]+troyka[1], troyka[0]+troyka[2], troyka[1]+troyka[2]]
        combinations = {x + y for x in k for y in pairs}
        k = {x%10: x for x in sorted(combinations)}.values()

    print(max(x for x in k if (((x%7 == 3 and x%10 != 5) or (x%7 != 3 and x%10 == 5)))))
