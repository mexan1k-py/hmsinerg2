#Homework 1
#print('Расчет площади и периметра прямоугольника!')
#b = float(input('Введите 1 сторону прямоугольника: '))
#a = float(input('Введите 2 сторону прямоугольника: '))

#c = a * b

#d = 2 * a + 2 * b

#print('Результат:','\nПлощадь прямоугольника =', c, '\nПериметр прямоугольника =', d)

#Homework 2
#a, b, c, d, e = map(int, input())

#f = ((d ** e) * c) / (a - b)

#print('Результат:', f)


#Урок №5. Логические и условные операторы
#Homework 1
a = int(input('Введите число: '))

if (a % 2 == 0) and ((a / 2) > 0):
    print('Положительное четное число')

if ((a % 2) != 0) and ((a / 2) > 0):
    print('Положительное нечетное число')

elif (a % 2 == 0) and ((a / 2) < 0):
    print('Отрицательное четное число')

elif (a % 2 != 0) and ((a / 2) < 0):
    print('Отрицательное нечетное число')

elif (a / 2 == 0):
    print('Нулевое число')

#Homework 2
slv = input('Введите слово: ')
ag = slv.count('a')
eg = slv.count('e')
ig = slv.count('i')
og = slv.count('o')
ug = slv.count('u')

glasn = ag + eg + ig + og + ug

if (ag == 0):
    print('Гласных "a" - False')
else:
    print('Гласных "a" -', ag)
if (eg == 0):
    print('Гласных "e" - False')
else:
    print('Гласных "e" -', eg)
if (ig == 0):
    print('Гласных "i" - False')
else:
    print('Гласных "i" -', ig)
if (og == 0):
    print('Гласных "o" - False')
else:
    print('Гласных "o" -', og)
if (ug == 0):
    print('Гласных "u" - False')
else:
    print('Гласных "u" -', ug)

print('Колличество гласных:', glasn)

print('Колличество согласных:', len(slv) - glasn)


#Homework 3
summ = int(input('Минимальная сумма взноса: '))

ivan = int(input('Сумма денег у Ивана: '))

maikl = int(input('Сумма денег у Майкла: '))

if (ivan >= summ) and (maikl >= summ):
    print(2)
elif (ivan >= summ) and (maikl <= summ):
    print('Ivan')
elif (maikl >= summ) and (ivan <= summ):
    print('Maikl')
elif (ivan <= summ) and (maikl <= summ) and ((ivan + maikl) > summ):
    print(1)
else:
    (ivan <= summ) and (maikl <= summ) and ((ivan + maikl) < summ)
    print(0)