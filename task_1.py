"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, time, salary, premium = argv


def salary_func():
    return int(time) * int(salary) + int(premium)


print(f"Зарплата: {salary_func()}")


'''
from sys import argv
name, time, salary, premium = argv

final_salary = int(time) * int(salary) + int(premium)
print("Зарплата: ", final_salary)
'''
