'''
Тип 14 № 48339

Операнды арифметического выражения записаны в системе счисления с основанием 11:

982x811 + 194x711

В записи чисел переменной x обозначена неизвестная цифра из алфавита одиннадцатиричной системы счисления.
Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 58.
Для найденного значения x вычислите частное от деления значения арифметического выражения на 58 и укажите его в ответе в десятичной системе счисления.
Основание системы счисления в ответе указывать не нужно.

'''


for x in '0123456789A': # выписываем значения до 11
    a = int('982' + x + '8', 11) + int('194' + x + '7', 11) # выписываем выражение
    if a % 58 == 0:
        print(a // 58)
        exit