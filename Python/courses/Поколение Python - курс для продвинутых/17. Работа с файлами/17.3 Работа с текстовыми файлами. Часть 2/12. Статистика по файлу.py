# https://stepik.org/lesson/530408/step/12
"""
Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей.
Напишите программу, которая выводит количество букв латинского алфавита, слов и строк.
Выведите три найденных числа в формате, приведенном в примере.
"""

with open('file.txt') as f:
    content = f.read()
    lines_n = content.count('\n') + 1
    words_n = len(content.split())
    alpha_n = len(''.join(filter(str.isalpha, content)))

    print('Input file contains:')
    print(f'{alpha_n} letters')
    print(f'{words_n} words')
    print(f'{lines_n} lines')

'''
---------------
Sample Input 1 (in file):
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Sample Output 1:
Input file contains:
108 letters 
20 words 
4 lines 
'''
