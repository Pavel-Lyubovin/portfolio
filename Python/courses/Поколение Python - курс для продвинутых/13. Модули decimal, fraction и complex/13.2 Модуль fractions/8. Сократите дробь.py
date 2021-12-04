# https://stepik.org/lesson/362369/step/8
"""
Даны два натуральных числа m и n. Напишите программу, которая сокращает дробь m/n и выводит ее.
"""

import fractions

print(fractions.Fraction(f"{input()}/{input()}"))

'''
---------------
Sample Input 1:
3
6

Sample Output 1:
1/2
---------------
Sample Input 2:
12
16

Sample Output 2:
3/4
---------------
Sample Input 3:
12
12

Sample Output 3:
1
---------------
Sample Input 4:
30
2

Sample Output 4:
15
'''