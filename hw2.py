# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print('Введите вещественное число:')
a = float(input())
str_a = str(a)
str_a = str_a.replace('.', '')
lst_str = list(str_a)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)