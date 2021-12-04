# https://stepik.org/lesson/362369/step/13
"""
На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания
все несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.
"""

from fractions import Fraction as F

res = set([F(n, d) for d in range(2, int(input()) + 1) for n in range(1, d)])
print(*sorted(res), sep='\n')

'''
---------------
Sample Input 1:
5

Sample Output 1:
1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
---------------
Sample Input 2:
4

Sample Output 2:
1/4
1/3
1/2
2/3
3/4
---------------
Sample Input 3:
3

Sample Output 3:
1/3
1/2
2/3
'''