'''
Тип 17 № 48465 (редкие)

Файл содержит последовательность целых чисел, по модулю не превышающих 10 000. Назовём парой два идущих подряд элемента последовательности.

Определите количество таких пар, в которых запись ровно одного элемента заканчивается цифрой 6,
а сумма квадратов элементов пары меньше, чем квадрат наименьшего из элементов последовательности, запись которых заканчивается цифрой 6.
В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму квадратов элементов этих пар.

'''

a = 0
b = 0
k = 0

c = open('17.4.txt')
t = [int(i) for i in c]

for i in range(len(t)):
    if abs(t[i]) % 10 == 6:
        k = min(k, t[i])

for i in range(len(t) - 1):
    if ((abs(t[i]) % 10 == 6 and (abs(t[i+1])) % 10 != 6) or ((abs(t[i])) % 10 != 6 and abs((t[i+1])) % 10 == 6)) and ((t[i]**2 + t[i+1]**2) < k**2):

        a += 1
        b = max(b, (t[i]**2 + t[i+1]**2 ))
print(a, b)
