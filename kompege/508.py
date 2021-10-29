with open('27-B (5).txt') as f:
    n = int(f.readline())

    k = [0]*101
    count = 0

    for i in range(n):
        x = int(f.readline())
        k[x] += 1

    save_not = [0]*2
    pairs = [0]*2

    for j in range(101):
        if k[j] > 0:
            save_not[j%2] += 1
            if k[j] > 1:
                pairs[j%2] += 1

    var1 = (save_not[0]*(save_not[0] - 1)//2) * (save_not[1]*(save_not[1] - 1)//2)
    var2 = pairs[0]*pairs[1]
    var3 = pairs[0]*(save_not[1]*(save_not[1] - 1)//2)
    var4 = (save_not[0]*(save_not[0] - 1)//2)*pairs[1]

    print(sum({var1, var2, var3, var4}))
                
        
      
        

       
