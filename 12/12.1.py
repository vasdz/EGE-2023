'''
Тип 12 № 10317

Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 125 идущих подряд цифр 8?
В ответе запишите полученную строку.

НАЧАЛО
ПОКА нашлось (333) ИЛИ нашлось (888) # 1
ЕСЛИ нашлось (333) # 2
ТО заменить (333, 8) # 3
ИНАЧЕ заменить (888, 3) # 4
КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

'''

a = '8' * 125
while('333' in a) or ('888' in a): # 1
    if '333' in a: # 2
        a = a.replace('333', '8', 1) # 3
    else:
        a = a.replace('888', '3', 1) # 4
print(a)
