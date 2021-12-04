# https://stepik.org/lesson/362369/step/10
"""
На вход программе подается натуральное число nnn. Напишите программу, которая вычисляет и выводит рациональное число,
равное значению выражения
1 / 1 ** 2 + 1 / 2 ** 2 + 1 / 3 ** 2 + ... + 1 / n ** 2
"""

from fractions import Fraction as F

n = int(input())
print(sum([F(1, i ** 2) for i in range(1, n + 1)]))

'''
---------------
Sample Input 1:
1

Sample Output 1:
1
---------------
Sample Input 2:
2

Sample Output 2:
5/4
---------------
Sample Input 3:
3

Sample Output 3:
49/36
---------------
Sample Input 4:
4

Sample Output 4:
205/144
---------------
Sample Input 5:
5

Sample Output 5:
5269/3600
'''