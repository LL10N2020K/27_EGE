def p(n):
        return all(n%j != 0 for j in range(2, int(n**0.5) + 1))

with open('27-82b.txt') as f:
    n = int(f.readline())
 
    k = [[0, 0]]
    s = 0

    for i in range(n):
        x = int(f.readline())
        combinations = [[a + x, b + p(x)] for a, b in k] + [[x, p(x)]]
        k = {x[1]%9: x for x in sorted(combinations)}.values()
 
        for a, b in k:
            s = max(a, s) if b%9 == 0 else s
                
    print(s)
 
 
