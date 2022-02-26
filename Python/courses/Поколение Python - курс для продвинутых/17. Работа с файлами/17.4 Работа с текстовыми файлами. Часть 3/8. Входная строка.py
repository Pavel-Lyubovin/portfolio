# https://stepik.org/lesson/519126/step/8
"""
Входная строка
Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.
"""

line = input()
with open('output.txt', 'w') as f:
    f.write(line)
