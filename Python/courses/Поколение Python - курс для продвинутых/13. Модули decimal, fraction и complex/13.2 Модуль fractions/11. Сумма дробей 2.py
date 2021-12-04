# https://stepik.org/lesson/362369/step/11
"""
На вход программе подается натуральное число nnn. Напишите программу, которая вычисляет и выводит рациональное число,
равное значению выражения
1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / n!
"""

from fractions import Fraction as F
from math import factorial

n = int(input())
print(sum([F(1, factorial(i)) for i in range(1, n + 1)]))

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
3/2
---------------
Sample Input 3:
3

Sample Output 3:
5/3
---------------
Sample Input 4:
4

Sample Output 4:
41/24
---------------
Sample Input 5:
5

Sample Output 5:
103/60
'''