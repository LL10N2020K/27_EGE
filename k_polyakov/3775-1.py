'''
Метод-шаблон для убийства задач по типу "Найти максимальную/минимальную сумму N чисел, кратную D".
Мы храним N минимальных/максимальных чисел по D остаткам = N*D чисел. Допустим, если нужно найти максимальную
сумму четвёрки чисел, кратную 6, тогда мы храним 4 максимальных числа с остатком от деления на 6 = 0, с остатком
от деления на 6 = 1, далее = 2, = 3, = 4 и = 5 соответственно. Всего 4*6 = 24 числа.
Далее из этих 24 чисел мы собираем всевозможные частичные суммы, ограничивая их длину (количество чисел, которыми
эти суммы образованы) до 5. Получаем список всевозможных сумм пар, троек и четверок. Выбираем оттуда максимум/минимум.
'''

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

print(max(x[0] for x in s if x[1] == 4 and x[0]%6 == 0))
        

#ИЛИ ЕЩЁ ОДНА РЕАЛИЗАЦИЯ, ПРОСТО ПЕРЕБИРАЕМ ВСЕ ЧЕТВЁРКИ!
 
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
 
s = 0
for x in range(len(t) - 3):
    for y in range(x + 1, len(t) - 2):
        for z in range(y + 1, len(t) - 1):
            for w in range(z + 1, len(t)):
                if (t[x]+t[y]+t[z]+t[w])%6 == 0:
                    s = max(s, t[x]+t[y]+t[z]+t[w])

print(s)
 
# И НАКОНЕЦ ЛУЧШАЯ РЕАЛИЗАЦИЯ


data = sorted(list(map(int, open('27-56b.txt').readlines()))[1:])[::-1]
 
s = [[0,0]]
for x in data:
    c = [y for y in s] + [[sm + x, ln + 1] for sm, ln in s if ln + 1 < 5] + [[x, 1]]
    s = {x[0]%6: x for x in sorted(c)}.values()

print(max(x[0] for x in s if x[1] == 4 and x[0]%6 == 0))

