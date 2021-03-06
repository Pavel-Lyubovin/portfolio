# https://stepik.org/lesson/508939/step/13
"""
Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
Напишите программу сортировки списка спортсменов по указанному полю:
    1: по имени;
    2: по возрасту;
    3: по росту;
    4: по весу.
"""


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def gen(s_type):
    def comp(tpl):
        return tpl[s_type - 1]
    return comp


sort_type = int(input())

f = gen(sort_type)
athletes.sort(key=f)
[print(*athlet) for athlet in athletes]


'''
---------------
Sample Input 1:
3

Sample Output 1:
Рустам 10 128 30
Дима 10 130 35
Тимур 11 135 39
Руслан 9 140 33
Матвей 17 168 68
Амир 16 170 70
Рома 16 188 100
Петя 15 190 90

---------------
Sample Input 2:
2

Sample Output 2:
Руслан 9 140 33
Дима 10 130 35
Рустам 10 128 30
Тимур 11 135 39
Петя 15 190 90
Амир 16 170 70
Рома 16 188 100
Матвей 17 168 68
'''