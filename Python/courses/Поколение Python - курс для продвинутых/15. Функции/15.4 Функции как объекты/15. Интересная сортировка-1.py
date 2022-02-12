# https://stepik.org/lesson/508939/step/15
"""
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.
"""


def sum_digits(str_num):
    return sum([int(char) for char in str_num])


str_nums = list(input().split())
print(*sorted(str_nums, key=sum_digits))

'''
---------------
Sample Input 1:
12 14 79 7 4 123 45 90 111

Sample Output 1:
12 111 4 14 123 7 45 90 79
---------------
Sample Input 2:
10 11 12 13 14 15 16 17 18 19 20 21 22 23

Sample Output 2:
10 11 20 12 21 13 22 14 23 15 16 17 18 19
'''