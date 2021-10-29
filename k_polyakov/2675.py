with open('27-15b.txt') as f:
    n = int(f.readline())

    k = [0]*14
    count = 0
    read = [int(f.readline()) for i in range(5)]

    for i in range(n - 5):
        x = int(f.readline())
        k[read[0]%14] += 1
        count += k[(14 - x%14)%14]
        read.append(x)
        read.remove(read[0])

    print(count)
