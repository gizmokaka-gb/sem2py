# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# (Сделать для строки)
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input('Введите число: '))
str_num = str(num)
str_num = str_num.replace('.','')
list_str = list(str_num)
list_num = map(int, list_str)
summ = sum(list_num)
print(f'Сумма: {summ}')