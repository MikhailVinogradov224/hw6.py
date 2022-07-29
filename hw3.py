# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
from functools import reduce
print('Введите n')
n = int(input())
print(reduce((lambda x,y: ((1 + 1/x))**x + ((1 + 1/y)**y)), (i for i in range(1,n) if i < (n+1))))