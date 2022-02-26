# https://stepik.org/lesson/530408/step/10
"""
Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать
одно или несколько целых чисел, разделенных одним или несколькими пробелами.
Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит
эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).
"""


with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))

'''
---------------
Sample Input 1 (in file):
2 1
     3    4
 1       7

Sample Output 1:
3
7
8
'''
