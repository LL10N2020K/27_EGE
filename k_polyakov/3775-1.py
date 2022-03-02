f = open('27-56b.txt')
n = int(f.readline())
data = sorted(map(int, f.readlines()))[::-1]
 
k = [0]*6
t = []
for j in range(6):
    for x in data:
        if x%6 == j:
            k[j] += 1
            t += [x]
        if k[j] >= 4:
            break
 
s = [[0,0]]
for x in t:
    c = s + [[sm + x, ln + 1] for sm, ln in s if ln + 1 < 5] + [[x, 1]]
    s = c
print(len(s))
print(max(x[0] for x in s if x[1] == 4 and x[0]%6 == 0))
        


