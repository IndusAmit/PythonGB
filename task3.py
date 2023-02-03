def my_func_sort():
    # Сумма двух наибольших чисел через sort()

    a, b, c = input(), input(), input()
    my_list = [a, b, c]
    my_list.sort()
    my_list.reverse()
    my_sum = int(my_list[0]) + int(my_list[1])
    return my_sum


print(my_func_sort())


def my_func_notsort():
    # Сумма двух наибольших чисел без sort()
    a, b, c = int(input()), int(input()), int(input())
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    return a + b


print(my_func_notsort())
