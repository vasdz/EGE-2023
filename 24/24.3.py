'''
Тип 24 № 27691

Текстовый файл состоит не более чем из 106 символов A, B и C.
Определите максимальное количество идущих подряд символов A.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

'''

a = 1
b = 0

c = open('24.3(1).txt').readline()

for i in range(len(c)-1):
    if c[i] == 'A' and c[i+1] == 'A': # можно подставить любую букву A, B, C (код универсален)
        a += 1
        b = max(b, a)

    else: a = 1
print(b)

