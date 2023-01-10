print('1. Введите два числа:')
a = input()
b = input()
print(a, b)
print('')


print('2. Введите время в секундах:')
a = int(input())
sec = a % 60
hour = a // 3600
b = a // 60
min = b % 60
if hour <= 23:
    print(hour, ":", min, ":", sec)
    print('')
else:
    print('За гранью возможного')


print('3. Введите число:')
a = input()
b = int(a) + int(a+a) + int(a*3)
print(b)
print('')


print('4. Введите целое положительное число:')
a = int(input())
b = 0
if a > 9:
    while a > 0:
        c = a % 10
        a //= 10
        if c > b:
            b = c
else:
    b = a
print(b)
print('')


print('5. Введите значение выручки и издержек')
a = int(input('Выручка:'))
b = int(input('Издержки:'))
if a > b:
    print('Выручка больше издержек')
else:
    print('Издержки больше выручки')
print('')


print('6. Подсчет рентабельности выручки:')
if a > b:
    c = a / b
    print('Рентабельность:', c)
    k = int(input('Введите количество сотрудников:'))
    s = a / k
    print('Прибыль фирмы в расчёте на одного сотрудника:', s)
print('')


print('7. Введите значения дистанции пробежки в первый день и желаемую дистанцию:')
a = int(input('Дистанция в 1-ый день:'))
b = int(input('Дистанция желаемая:'))
i = 1
print('1-й день:', a)
while b > a:
    a += a * 0.1
    a = int(a * 100) / 100
    i += 1
    print(str(i)+'-й день:', a)
