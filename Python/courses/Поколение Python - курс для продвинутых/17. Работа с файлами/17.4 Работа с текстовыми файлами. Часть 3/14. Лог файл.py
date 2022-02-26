# https://stepik.org/lesson/519126/step/14
"""
Лог файл
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
Каждая строка файла содержит три значения, разделенные запятыми и символом пробела:
имя пользователя, время входа, время выхода, где время указано в 24-часовом формате.
Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
(не меняя порядка следования), которые были в сети не менее часа.
"""

from datetime import datetime

with open('logfile.txt') as imp_f, open('output.txt', 'w') as out_f:
    for line in imp_f:
        name, time1, time2 = line.rstrip().split(', ')
        time1_ = datetime.strptime(time1, '%H:%M')
        time2_ = datetime.strptime(time2, '%H:%M')
        diff = (time2_ - time1_).seconds
        if diff >= 3600:
            print(name, file='out_f')


'''
---------------
Sample Input 1 (in file):
Тимур Гуев, 14:10, 15:50
Руслан Гриценко, 12:00, 12:59
Роман Гацалов, 09:10, 17:45
Габолаев Георгий, 11:10, 12:10

Sample Output 1 (in file):
Тимур Гуев
Роман Гацалов
Габолаев Георгий
'''