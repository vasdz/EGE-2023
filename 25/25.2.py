'''
(№ 5281) (А. Агафонцев) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Найдите наименьшие 7 чисел, удовлетворяющих маске ?6*6*?6 и при этом кратных 6, 7 и 8.
Выведите эти числа в порядке возрастания, справа от каждого числа выведите сумму его делителей.

**kpolyakov
'''

from fnmatch import *

def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d) # множество всех делителей

for x in range(10**6): # Переберем числа до 10**6 (взять с избытком т.к. 10**5 не достаточно)
    if fnmatch(str(x),'?8*8*?8') and x%6 == 0 and x%7 == 0 and x%8 == 0: # Подставим маску
        print(x, sum(div(x))) # сумма делителей ( в ответ пойдут только первые 7 пар цисел т.к. требуются наименьшие )