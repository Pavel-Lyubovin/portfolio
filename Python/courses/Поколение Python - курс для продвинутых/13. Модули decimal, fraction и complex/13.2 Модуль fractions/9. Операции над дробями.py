# https://stepik.org/lesson/362369/step/9
"""
Даны две дроби в формате a/b. Напишите программу,
которая вычисляет и выводит их сумму, разность, произведение и частное.
"""

from fractions import Fraction as F

num1, num2 = input(), input()
frac1, frac2 = F(num1), F(num2)
print(num1, '+', num2, '=', frac1 + frac2)
print(num1, '-', num2, '=', frac1 - frac2)
print(num1, '*', num2, '=', frac1 * frac2)
print(num1, '/', num2, '=', frac1 / frac2)

'''
---------------
Sample Input 1:
2/3
3/7

Sample Output 1:
2/3 + 3/7 = 23/21
2/3 - 3/7 = 5/21
2/3 * 3/7 = 2/7
2/3 / 3/7 = 14/9
---------------
Sample Input 2:
3/4
1/4

Sample Output 2:
3/4 + 1/4 = 1
3/4 - 1/4 = 1/2
3/4 * 1/4 = 3/16
3/4 / 1/4 = 3
---------------
Sample Input 3:
5/10
10/5

Sample Output 3:
5/10 + 10/5 = 5/2
5/10 - 10/5 = -3/2
5/10 * 10/5 = 1
5/10 / 10/5 = 1/4
'''