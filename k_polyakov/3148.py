with open('27-42a.txt') as f:
  n = int(f.readline())

  s1 = s2 = s3 = k0 = 0
  k1 = [[float('inf'), float('-inf')], [float('inf'), float('-inf')]]
  k2 = [[float('inf'), float('-inf')], [float('inf'), float('-inf')]]

  for j in range(n):
    x, y, z = sorted(map(int, f.readline().split()))
    s1 += x
    s2 += y
    s3 += z

    if (y - x)%2:
      k0 = 1
    if (z - x)%2:
      min_razn = z - x
      if (z - y)%2:
        min_razn = z - y
      if min_razn < k1[0][0]:
        k1 = [[min_razn, j], k1[0]]
      elif min_razn < k1[1][0]:
        k1[1] = [min_razn, j]
    if (z - y)%2:
      min_razn = z - y
      if min_razn < k2[0][0]:
        k2 = [[min_razn, j], k2[0]]
      elif z - y < k2[1][0]:
        k2[1] = [min_razn, j]

  if s1%2 == 0  and  s2%2 == 0:
    print(s3)
  elif s1%2 != 0 and s2%2 != 0:
    if k0:
      print(s3)
    else:
      cur_min = min([k1[0][0] + k2[1][0], k1[1][0] + k2[0][0], k1[0][0] + k1[1][0], k2[0][0] + k2[1][0]])
      if k1[0][1] != k2[0][1]:
        cur_min = min([cur_min, k1[0][0] + k2[0][0]])
      print(s3 - cur_min)
  elif s1%2:
    k0 = k1[0][0]
    if k0:
      if len(k0) > 1 or k2[0][1] != k0[0]:
        cur_min2 = min(cur_min2, k2[0][0] )
      elif k2[1][1] != k0[0]:
        cur_min2 = min(cur_min2, k2[1][0] )
    print(s3 - cur_min2)
  elif s2%2:
    print(s3 - k2[0][0])
