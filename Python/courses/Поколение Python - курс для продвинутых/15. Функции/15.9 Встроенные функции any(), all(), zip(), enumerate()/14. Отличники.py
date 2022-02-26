# https://stepik.org/lesson/511854/step/14
"""
Отличники
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK
и решил убедиться, что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе.
Напишите программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.
"""


klasses = []
for kl in range(int(input())):
    grades = []
    for st in range(int(input())):
        name, grade = input().split()
        grades.append(int(grade))
    klasses.append(any(gr == 5 for gr in grades))
print(('NO', 'YES')[all(klasses)])


'''
---------------
Sample Input 1:
4
3
Васечкин 4
Илюшин 5
Кривцов 3
2
Боталов 5
Петров 5
3
Лебеда 4
Ивлев 4
Суворов 5
2
Ласкер 4
Козлов 5

Sample Output 1:
YES
---------------
Sample Input 2:
4
3
Васечкин 4
Илюшин 5
Кривцов 3
2
Боталов 5
Петров 5
3
Лебеда 4
Ивлев 4
Суворов 4
2
Ласкер 4
Козлов 5

Sample Output 2:
NO
'''
