# https://stepik.org/lesson/530408/step/13
"""
Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия,
а затем выводит их, каждую на отдельной строке.
"""

from random import choice

with open('first_names.txt') as f_name, open('last_names.txt') as l_name:
    first_names = f_name.readlines()
    last_names = l_name.readlines()
    for _ in range(3):
        print(choice(first_names).rstrip(), choice(last_names).rstrip())

'''
---------------
Sample Input 1 (in files):
Aaron
Abdul
Abe
Abel
Abraham
Albert

и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein

Sample Output 1 (possible variant):
Abdul Albertson
Abel Adamson
Albert Einstein
'''
