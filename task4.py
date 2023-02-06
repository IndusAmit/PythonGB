with open(r"D:\Git\backup\lesson5\task4_salary.txt", "r", encoding="utf8") as my_file:
    board = 20000.00
    my_sum = 0.00
    c = 0
    print('Люди, зарабатывающте менее 20000 рублей:')
    for line in my_file:
        a = line.split(" ")
        sal = float(a[1])
        if sal < board:
            surn = a[0]
            print(surn)
        my_sum += sal
        c += 1
    print(f"Средений оклад: {format(my_sum/c, '.2f')}")
