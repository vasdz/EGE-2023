'''
Тип 14 № 48435

В выражении 1xBAD16+2CxFE16 x обозначает некоторую цифру из алфавита шестнадцатеричной системы счисления.
 Определите наименьшее значение x, при котором значение данного выражения кратно 15.
 Для найденного x вычислите частное от деления данного выражения на 15 и запишите его в ответе в десятичной системе счисления.

'''

a = []
for x in '0123456789ABCDEF': # выписываем значения до 16
    for y in '0123456789ABCDEF': # выписываем значения до 16
        b = int('1' + x + 'BAD', 16) + int('2C' + x + 'FE', 16)
        if b % 15 == 0:
            a.append(b) # добавляем в конец аргумент
if a:
    print(min(a) // 15)