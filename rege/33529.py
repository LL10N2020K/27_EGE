with open('27-B (6).txt') as f:
    n = int(f.readline())

    max_s = 0
    nechet = 0
    k = [[float('inf'),float('inf')],[float('inf'),float('inf')]]
  
    for i in range(n):
      x, y = sorted(map(int, f.readline().split()), reverse = True)
      max_s += x
      nechet += x%2
      if x%2 != y%2:
        k[y%2].append(x - y)

    chet = n - nechet
    min_chet = min_nechet = 0
    k[0] = sorted(k[0])[:2]
    k[1] = sorted(k[1])[:2]

    if max_s%2 == (chet > nechet):
      if (nechet - chet) > 1:
        min_chet = k[0][0]
        min_nechet = k[1][0]
      elif chet > nechet: 
        min_chet = k[0][0] 
        min_nechet = k[1][0] + k[1][1] 
      else: 
        min_nechet = k[1][0] 
        min_chet = k[0][0] + k[0][1] 

    print(max_s - min(min_chet, min_nechet))
