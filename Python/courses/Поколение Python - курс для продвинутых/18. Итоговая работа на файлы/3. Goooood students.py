# https://stepik.org/lesson/448983/step/3
"""
Goooood students
Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров.
Строки файла имеют вид: фамилия оценка_1 оценка_2 оценка_3.
Напишите программу для подсчета количества студентов, сдавших все три теста.
Тест считается сданным, если количество баллов по нему не меньше 65.
"""

with open('grades.txt') as f:
    res = 0
    for line in f:
        chunks = line.split()
        pass_grades = list(filter(lambda x: x>= 65, map(int, chunks[1:])))
        if len(pass_grades) == 3:
            res += 1
    print(res)


'''
---------------
Sample Input 1 (in file):
Washington 83 77 54
Adams 86 69 90
Jacobson 50 49 71
MacDonald 100 99 100
Berrington 66 67 64

Sample Output 1:
2
'''