with open('27_B.txt') as f:
    n = int(f.readline())

    k = {0}

    for i in range(n):
        troyka = list(map(int, f.readline().split()))
        combinations = {x + y for x in k for y in troyka}
        k = {x%109: x for x in sorted(combinations)}.values()

    print(max(x for x in k if x%109 != 0))


   
