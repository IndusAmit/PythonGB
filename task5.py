def my_func():
    my_sum = 0
    x = 'a'
    print("Введите ! для выхода.")
    while x != '!':
        my_list = input("Введите числа: ").split(" ")
        now_sum = 0
        for i in range(len(my_list)):
            if my_list[i] == '!':
                x = '!'
                break
            else:
                try:
                    now_sum += int(my_list[i])
                except ValueError:
                    return ("Некорректный ввод данных!")
        my_sum += now_sum
    return f"Сумма введенных чисел равна {my_sum}"


print(my_func())
