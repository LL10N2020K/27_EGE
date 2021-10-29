with open('27-45b.txt') as f:
    n = int(f.readline())

    k = [0]*3
    r = []
    
    for i in range(n):
        troyka = sorted(list(map(int, f.readline().split()))) 

        for y in range(3):
            k[y] += troyka[y] 
  
        r_new = []
        if troyka[0]%2 != troyka[1]%2:
            r_new.append(abs(troyka[0] - troyka[1]))
        if troyka[0]%2 != troyka[2]%2:
            r_new.append(abs(troyka[0] - troyka[2]))
        if len(r_new) >= 1:
            r.append(min(r_new))
       
    r = sorted(r)[:2]
     
print(k[0] + sum(r)) 
