'''
Тип 23 № 13606

Первая команда увеличивает число на экране на 1, вторая – умножает его на 2, третья – умножает на 3.

Программа для исполнителя А17 – это последовательность команд.

Сколько существует программ, для которых при исходном числе 2 результатом является число 28 и при этом траектория вычислений содержит число 14?

Траектория вычислений программы – это последовательность результатов выполнения всех команд программы.
Например, для программы 121 при исходном числе 7 траектория будет состоять из чисел 8, 16, 17.

'''

def f(x, y):
    if x > y: # обязательный этап 1
        return 0
    if x == y: # обязательный этап 2
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y) # по условию

print(f(2, 14) * f(14, 28))
