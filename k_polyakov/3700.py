with open('27-49a.txt') as f:
  n = int(f.readline())

  min_s = 0
  nechet = 0
  k = [[float('inf'),float('inf')],[float('inf'),float('inf')]]
  
  for i in range(n):
    x, y = sorted(map(int, f.readline().split()))
    min_s += x
    nechet += x%2
    if x%2 != y%2:
      k[y%2].append(y - x)

  chet = n - nechet
  min_chet = min_nechet = 0
  k[0] = sorted(k[0])[:2]
  k[1] = sorted(k[1])[:2]

  if min_s%2 == (chet > nechet):
    if (nechet - chet) > 1:
      min_chet = k[0][0]
      min_nechet = k[1][0]
    elif chet > nechet: 
      min_chet = k[0][0] 
      min_nechet = k[1][0] + k[1][1] 
    else: 
      min_nechet = k[1][0] 
      min_chet = k[0][0] + k[0][1] 

  print(min_s + min(min_chet, min_nechet))

'''
with open('27-49b.txt') as f:
    n = int(f.readline())

    r = []
    mini = count_nechet = 0

    for i in range(n):
        pair = list(map(int, f.readline().split()))
        mini += min(pair)
        count_nechet += min(pair)%2
        if abs(pair[0] - pair[1])%2 != 0:
            r.append(abs(pair[0] - pair[1]))

    r.sort()
    count_chet = n - count_nechet


    j = 0
    while mini%2 == 0 and count_nechet >= count_chet or mini%2 != 0 and count_chet >= count_nechet:
        mini += r[j]
        if count_chet > count_nechet:
            count_chet += 1
            count_nechet += 1
        else:
            count_chet += 1
            count_nechet -= 1

    print(mini)
'''  
