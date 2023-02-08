new_file = open("task5.txt", "x")
with open("task5.txt", "w+", encoding='utf-8') as my_file:
    my_str = input("Введите числа через пробел: ")
    x = 0
    my_file.write(my_str)
    ciphers = my_str.split(' ')
    for i in ciphers:
        x += int(i)
    print(x)
