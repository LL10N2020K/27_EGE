with open('27B.txt') as f:
    next(f)

    a, ml = [int(x) for x in f if x != '\n'], 0

    for j in range(len(a) - 2):
        if a[j+2] - a[j+1] == a[j+1] - a[j]:
            d, l = [a[j+1], a[j]], 0
            while a[j+2+l] - a[j+2+l-1] == a[j+1] - a[j]:
                d.append(a[j+2+l])
                l += 1
            ml = max(ml, len(d)) if sum(d)%7 == 0 else ml
            
    print(ml)


