with open('27-70b.txt') as f:
    n = int(f.readline())

    s_max = s_min = {0}

    for _ in range(n):
        pair = list(map(int, f.readline().split()))
        combo_max = {(x+y) for x in pair for y in s_max}
        s_max = {x%5: x for x in sorted(combo_max)}.values()
        combo_min = {(x+y) for x in pair for y in s_min}
        s_min = {x%5: x for x in sorted(combo_min)[::-1]}.values()

    print([x for x in s_max][0] - [x for x in s_min][0])

        
