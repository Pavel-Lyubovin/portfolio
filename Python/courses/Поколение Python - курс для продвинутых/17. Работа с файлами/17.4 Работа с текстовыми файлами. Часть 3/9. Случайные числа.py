# https://stepik.org/lesson/519126/step/9
"""
Случайные числа
Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел
в диапазоне от 111 до 777 (включительно), каждое с новой строки.
"""

from random import randint


with open('random.txt', 'w') as f:
    for _ in range(25):
        print(randint(111, 777), file=f)
