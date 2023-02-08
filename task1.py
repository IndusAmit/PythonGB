x = True
my_file = open('my_file.txt', 'w')
print('Для завершения введите пустую строку')
while x == True:
    c = input("Введите строку: ")
    my_file.writelines(f"{c} \n")
    if c == '':
        break
my_file.close()
