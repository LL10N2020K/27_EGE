Сложное в понимании решение (старое):
    
with open('27-19b.txt') as f:
    n = int(f.readline())

    count = mini = maxi = 0
    
    for i in range(n):
        x = int(f.readline())
        cur_min = min(mini*x, maxi*x, x)
        maxi = max(mini*x, maxi*x, x)
        mini = cur_min
        count = max(count, maxi)

    print(count)

Новое решение, более логичное и ясное:
    
with open('27-19b.txt') as f:
    n = int(f.readline())
    
    Pcur, Pmax = 0, 0
    
    for i in range(n):
        x = int(f.readline())
        if x == 0:
            Pcur = 1
        else:
            Pcur = Pcur * x 
        Pmax = max(Pcur, Pmax)
        
    print(Pmax)

