# https://stepik.org/lesson/519126/step/13
"""
Конкатенация файлов
На вход программе подается натуральное число n и n строк с названиями файлов.
Напишите программу, которая создает файл output.txt и выводит в него
содержимое всех файлов с указанными именами, не меняя их порядка.
"""

n = int(input())
with open('output.txt', 'w') as out_f:
    for _ in range(n):
        with open(input()) as f:
            out_f.write(f.read())

'''
---------------
Sample Input 1 (in file):
Содержимое 1 файла:
Python
c++

Содержимое 2 файла:
c#
php

Sample Output 1 (in file):
Результат:
python
c++c#
php
'''