def sum_of_digits(x): 
    s = 0
    for j in range(len(x)):
        s += int(x[j])
    return s

with open('27-39b.txt') as f:
    n = int(f.readline())

    k = [0] * 1000
    yes = [False] * 1000
    s = 0
    central = 0

    for _ in range(n):
        k[int(f.readline())] += 1

    for i in range(999, 99, -1):
        n1 = str(i)[::-1]
        if (k[i] != 0) and (k[int(n1)] != 0):
            n2 = min(k[i], k[int(n1)])
            n3 = n2
            if i != int(n1):
                n2 += n2
            elif n2 % 2 == 1:
                n2 -= 1
            if n2 > 1:
                if (not yes[i]) and (not yes[int(n1)]):
                    if n2 % 2 == 0:
                        s += (n2//2) * (sum_of_digits(str(i)) + sum_of_digits(str(n1)))
                        yes[i], yes[int(n1)] = True, True
            if (i > central) and (n3 % 2 == 1) and (i == int(n1)):
                central = i

    print(s + sum_of_digits(str(central)))
