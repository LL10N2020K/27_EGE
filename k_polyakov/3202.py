with open('27-47a.txt') as f:
    n = int(f.readline())

    k = {0}
    s = 0
    
    for _ in range(n):
        pair = list(map(int, f.readline().split()))
        s += max(pair)
        combinations = {x + y  for x in k for y in pair}
        k = {x%10: x for x in sorted(combinations)[::-1]}.values()

    print(min(x for x in k if x%10 == s%10))
