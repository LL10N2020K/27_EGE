with open('27-14b.txt') as f:
    n = int(f.readline())

    k = [0]*12
    count = 0

    for i in range(n):
        x = int(f.readline())
        count += k[(12 - x%12)%12]
        k[x%12] += 1

    print(count)
