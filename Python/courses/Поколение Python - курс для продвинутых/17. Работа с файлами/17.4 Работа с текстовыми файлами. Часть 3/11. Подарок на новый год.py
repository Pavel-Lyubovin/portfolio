# https://stepik.org/lesson/519126/step/11
"""
Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида:
фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.
Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий
и новых результатов тестов в файл new_scores.txt.
"""

with open('class_scores.txt') as imp_f, open('new_scores.txt', 'w') as out_f:
    for line in imp_f:
        name, score = line.split()
        print(name, min(100, int(score) + 5), file=out_f)

'''
---------------
Sample Input 1 (in file):
Washington 83
Adams 86
Kingsman 100
MacDonald 95
Thomson 98

Sample Output 1 (in file):
Washington 88
Adams 91
Kingsman 100
MacDonald 100
Thomson 100
'''