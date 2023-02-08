import json
with open("task7.txt", "r", encoding="utf-8") as obj:
    firm_dictionary = {}
    my_str = 'average_profit'
    dict_profit = {}
    sum_profit = 0
    c = 0
    my_lst = []
    for line in obj:
        c += 1
        x = line.split(' ')
        profit = int(x[2]) - int(x[3])
        sum_profit += profit
        if profit < 0:
            sum_profit -= profit
            c -= 1
        firm_dictionary[x[0]] = profit
    print(sum_profit)
    average_profit = int(sum_profit / c)
    dict_profit[my_str] = average_profit
    my_lst = [firm_dictionary, dict_profit]
    print(my_lst)

with open("task7.json", "w") as json_file:
    json.dump(my_lst, json_file)
