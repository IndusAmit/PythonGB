name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year = input('Введите год рождения: ') + ' года рождения'
place = ', проживает в городе ' + input('Введите город проживания: ')
e_mail = ', e-mail: ' + input('Введите e-mail: ')
phone = ', телефон: ' + input('Введите телефон: ')


def my_func(name, last_name, year, place, e_mail, phone):
    return ' '.join([name, last_name, year, place, e_mail, phone])


print(my_func(name, last_name, year, place, e_mail, phone))
