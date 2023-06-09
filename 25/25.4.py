'''
	(№ 5031) (Б. Михлин) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
- символ «?» означает ровно одну произвольную цифру;
- символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425. Найдите все натуральные числа, делящиеся нацело на 7916, шестнадцатеричный код которых соответствует маске 1?DED?CED.
В ответе запишите найденные числа в десятичной системе счисления в порядке убывания, а справа от каждого числа – соответствующее частное от деления на 7916.

**kpolyakov
'''

b = []
for c1 in '0123456789abcdef': # шестнадцатеричный код включает в себя
    for c2 in '0123456789abcdef': # шестнадцатеричный код включает в себя
        a = int(f'1{c1}ded{c2}ced', 16) # подставим выражение и 16
        if a%121 == 0: # 79 в 16 системе => 121
            # int('79',16) => код для счёта числа
            b += [(a,a//121)]
for x in b[::-1]:
    print(*x) # в ответ пойдут все пары чисел
