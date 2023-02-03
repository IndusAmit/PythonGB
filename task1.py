def my_func():
    try:
        numb_1 = int(input('Введите первое число: '))
        numb_2 = int(input('Введите второе число: '))
        my_var = numb_1 / numb_2
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    except ValueError:
        return "Неверный ввод"
    return my_var


print(my_func())
