with open('27-B (2).txt') as f:
    n = int(f.readline())

    k_razn_ost = [0]*3
    k_ost_1 = []
    k_ost_2 = []
    k_del = []
    

    for i in range(n):
        x = int(f.readline())
        if x%3 == 1:
            k_ost_1.append(x)
        if x%3 == 2:
            k_ost_2.append(x)
        if x%3 == 0:
            k_del.append(x)

        k_razn_ost[x%3] = max(k_razn_ost[x%3], x)

    k_ost_1 = (sorted(k_ost_1, reverse = True))[:3]
    k_ost_2 = (sorted(k_ost_2, reverse = True))[:3]
    k_del = (sorted(k_del, reverse = True))[:3]

    print(max(sum(k_ost_1), sum(k_ost_2), sum(k_del), sum(k_razn_ost)))


   
        
