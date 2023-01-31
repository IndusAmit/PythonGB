my_str = input("Введите слова через пробел: ")
my_word = []
ind = 0
my_word = my_str.split()
for ind, el in enumerate(my_word):
    if len(str(my_word)) <= 10:
        print(el)
    else:
        print(el[0:10])
