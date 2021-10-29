with open('27-50a.txt') as f:
    n = int(f.readline())

    k = [0]*2
    s = 0
    mini = []
    
    for i in range(n):
        x, y = map(int, f.readline().split())
        s += max(x, y)
        k[(max(x, y))%2] += 1
        if (x%2 != y%2):
            mini.append(abs(x - y))

    if max(k) != k[s%2]:
        print(s)
    else:
         print(s - min(mini))
  

