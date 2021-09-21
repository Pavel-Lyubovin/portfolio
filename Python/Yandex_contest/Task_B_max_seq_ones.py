'''
B. Последовательно идущие единицы

Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.

Формат ввода
Первая строка входного файла содержит одно число n, n ≤ 10000. Каждая из следующих n строк содержит ровно одно число — очередной элемент массива.

Формат вывода
Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц во входном массиве.

-------------
Simple input:

5
1
0
1
0
1

-------------
Simple output:

1
-------------
'''

n = int(input())
cur_seq = 0
max_seq = 0
for _ in range(n):
    num = int(input())
    if num == 1:
        cur_seq += 1
        max_seq = max(cur_seq, max_seq)
    else:
        cur_seq = 0
print(max_seq)
