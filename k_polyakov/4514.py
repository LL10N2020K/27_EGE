with open('27-81b.txt') as f:
    n = int(f.readline())
 
    k = [[0, 0]]
    s = 0

    for i in range(n):
        x = int(f.readline())
        combinations = [[a + x, b + x%2] for a, b in k] + [[x, x%2]]
        k = {x[1]%13: x for x in sorted(combinations)}.values()
 
        for a, b in k:
            s = max(a, s) if b%13 == 0 else s
                
    print(s)
 
 
