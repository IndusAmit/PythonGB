x = int(input('Введите положительное число: '))
y = int(input('Введите его степень (отрицательное число): '))


def my_func(x, y):
    if x == 0:
        return('Число должно быть положительным!')
    if y >= 0:
        return('Степень должна быть отрицательной!')
    y *= -1
    s = 1
    for i in range(y):
        s = s * x
    return(1 / s)


print(my_func(x, y))
