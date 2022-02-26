# https://stepik.org/lesson/448983/step/8
"""
Пропущенные комменты
При написании собственных функций рекомендуется в комментарии описывать назначение функции,
ее параметры и возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок,
а потом и вовсе забывают о них.
На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python.
Напишите программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий.
Будем считать, что любая строка, начинающаяся со слова def и пробела, является началом определения функции.
Функция содержит комментарий, если первый символ предыдущей строки - #.
"""


f_name = input()
with open(f_name) as f:
    com_idx, def_idx = [], []
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('#'):
            com_idx.append(i)
        if line.startswith('def'):
            def_idx.append(i)
    no_comm = []
    for idx in def_idx:
        if idx - 1 not in com_idx:
            l_i = lines[idx].find('(')
            no_comm.append(lines[idx][4:l_i])
    if len(no_comm):
        print(*no_comm, sep='\n')
    else:
        print('Best Programming Team')


'''
---------------
Sample Input 1 (in file):
def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0  
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count
    
def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

Sample Output 1 (in file):
powers
matrix
mean
greet
'''