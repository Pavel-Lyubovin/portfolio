# https://stepik.org/lesson/512854/step/16
"""
Многочленом степени n называется выражение вида
a_n * x ** n + a_n−1 * x ** n−1 + … + a_2 * x ** 2 + a_1 * x + a_0
На вход программе на первой строке подаются коэффициенты многочлена,
разделенные символом пробела и целое число x на второй строке.
Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.
"""

from functools import reduce

def evaluate(coefficients, x):
    seq = map(lambda c: c[1] * x ** c[0], enumerate(coefficients[::-1]))
    res = reduce(lambda x, y: x + y, seq)
    return res


coefficients = list(map(int, input().split()))
x = int(input())

print(evaluate(coefficients, x))

'''
---------------
Sample Input 1:
2 4 3
10

Sample Output 1:
243
---------------
Sample Input 2:
1 2 3 4 5 6 7
1

Sample Output 2:
28
---------------
Sample Input 3:
-2 4 5
3

Sample Output 3:
-1
---------------
Sample Input 4:
10
2

Sample Output 4:
10
---------------
Sample Input 5:
3 19
10

Sample Output 5:
49
'''
