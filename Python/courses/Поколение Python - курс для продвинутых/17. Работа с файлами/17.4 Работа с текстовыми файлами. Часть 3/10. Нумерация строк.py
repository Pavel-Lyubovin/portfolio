# https://stepik.org/lesson/519126/step/10
"""
Нумерация строк
Вам доступен текстовый файл input.txt, состоящий из нескольких строк.
Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка,
где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.
"""

with open('input.txt') as inp_f, open('output.txt', 'w') as out_f:
    for i, line in enumerate(inp_f, start=1):
        out_f.write(str(i) + ') ' + line)


'''
---------------
Sample Input 1 (in file):
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Sample Output 1 (in file):
1) Beautiful is better than ugly.
2) Explicit is better than implicit.
3) Simple is better than complex.
4) Complex is better than complicated.
'''