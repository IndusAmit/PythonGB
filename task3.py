my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open(r"D:\Git\backup\lesson5\task3.txt", "r", encoding='utf-8') as fi:
    for line in fi:
        for key in my_dict.keys():
            line = line.replace(key, my_dict[key])
        with open("task3_2.txt", "a") as text_file:
            text_file.write(f"\n {line}")
