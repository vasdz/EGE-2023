'''
Тип 8 № 10473 (редкие задачи)

Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 4.
 Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза,
  а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

'''
from itertools import product

a = '1234' # алфавит
k = 0
for i in product(a, repeat=5):
    if i.count('1') == 2: # по условию
        k += 1
print(k)