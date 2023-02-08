my_file = open("task2.txt", "r")
print(f"Количество строк в файле: {len(my_file.readlines())}")
k = 0
my_file.close()

my_file = open("task2.txt", "r")
s = my_file.readlines()
for i in range(len(s)):
    k = len(s[i].split(" "))
    print(f"Количество слов в строке {i+1} - {k}")
my_file.close()
