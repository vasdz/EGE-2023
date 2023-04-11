'''
Тип 16 № 35474

Обозначим через mod(a, b) остаток от деления натурального числа a на натуральное число b.
Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:

F(0) = 0; # 1
F(n) = F(n / 3), если n > 0 и при этом mod(n, 3)=0; # 2
F(n) = mod(n, 3) + F(n − mod(n, 3)), если mod(n, 3) > 0. # 3

Назовите минимальное значение n, для которого F(n) = 11
'''

def F(n):
    if n == 0: # 1
        return 0
    if n % 3 == 0 and n > 0: # 2 ; mod(n, 3) => n % 3
        return F(n / 3)
    if n % 3 > 0: # 3
        return n % 3 + F(n - (n % 3))
i = 0
while F(i) != 11:
    i += 1
print(i)
