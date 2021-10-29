def p(n):
    if n%5 == 0:
        return 1
    else:
        return 0

with open('27-80b.txt') as f:
    n = int(f.readline())
 
    k = [[0, 0]]
    s = 0

    for i in range(n):
        x = int(f.readline())
        combinations = [[a + x, b + p(x)] for a, b in k] + [[x, p(x)]]
        k = {x[1]%3: x for x in sorted(combinations)}.values()
 
        for a, b in k:
            s = max(a, s) if b%3 == 0 else s
                
    print(s)
 
 
