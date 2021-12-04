# https://stepik.org/lesson/360941/step/13
"""
На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения:
e ** d  +  ln(d)  +  lg(d)  +  sqrt(d)


"""

import decimal


d = decimal.Decimal(input())
print(d.exp() + d.ln() + d.log10() + d.sqrt())

'''
---------------
Sample Input 1:
1.1

Sample Output 1:
4.189677737079134559844013562
---------------
Sample Input 2:
4.0

Sample Output 2:
58.58650438559209208737220323
'''