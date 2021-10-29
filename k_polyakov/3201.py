with open('27-46b.txt') as f:
    n = int(f.readline())

    k = {0}
    s = 0
    
    for _ in range(n):
        pair = list(map(int, f.readline().split()))
        s += min(pair)
        combinations = {x + y  for x in k for y in pair}
        k = {x%7: x for x in sorted(combinations)}.values()

    print(max(x for x in k if x%7 == s%7))
