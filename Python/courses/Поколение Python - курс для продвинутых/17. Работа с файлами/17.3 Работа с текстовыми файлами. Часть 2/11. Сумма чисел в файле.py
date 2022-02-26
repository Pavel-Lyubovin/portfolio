# https://stepik.org/lesson/530408/step/11
"""
Сумма чисел в файле
Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числаи все, что угодно.
Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).
Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.
"""

with open('nums.txt') as f:
    sum_num = 0
    for line in f:
        sum_num += sum(map(int, ''.join([c if c.isdigit() else ' ' for c in line]).split()))
    print(sum_num)

'''
---------------
Sample Input 1 (in file):
 123   jhjk
bhjip456qwerty
1x2y3 4 5 6
sfsd 0 dfgfd
10abc20de30pop5 5 5 5

Sample Output 1:
680
'''
