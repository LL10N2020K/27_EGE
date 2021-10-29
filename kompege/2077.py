with open('27B.txt') as f:
    n = int(f.readline())

    k = [[0,0], [0,0], [0,0]]
    s = count = 0
    
    x_first = int(f.readline())
    
    for _ in range(n - 1):
        x_next = int(f.readline())
        ost = (3 - x_next%3)%3
        s = s + x_first
        count = count + k[ost][s%2]
        k[x_first%3][s%2] += 1
        x_first = x_next

    print(count)
  
