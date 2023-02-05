from functools import reduce

lst = [i for i in range(100, 1001) if i % 2 == 0]
my_func = lambda el_1, el_2: el_1 * el_2

print(reduce(my_func, lst))
