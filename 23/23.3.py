'''
Тип 23 № 6965

Первая из них увеличивает число на экране на 1, вторая удваивает его.
Программа для Удвоителя — это последовательность команд.
Сколько есть программ, которые число 2 преобразуют в число 22?

'''

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1

    return f(x + 1, y) + f(x * 2, y)
print(f(2, 22))
