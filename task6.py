num = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
final_list = {}
while n <= num:
    my_dict = dict({'название': input("Название "), 'цена': input("Цена "),
                    'количество': input('Количество '), 'eд': input("Единица измерения ")})
    my_list.append((n, my_dict))
    n += 1
    final_list = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'),
         'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(final_list)
