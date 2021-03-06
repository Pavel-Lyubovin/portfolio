# https://stepik.org/lesson/360942/step/12
"""
Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.
"""

n1, n2 = complex(input()), complex(input())
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")

'''
---------------
Sample Input 1:
1+2j
-2+4j

Sample Output 1:
(1+2j) + (-2+4j) = (-1+6j)
(1+2j) - (-2+4j) = (3-2j)
(1+2j) * (-2+4j) = (-10+0j)
---------------
Sample Input 2:
-1-1j
-1+1j

Sample Output 2:
(-1-1j) + (-1+1j) = (-2+0j)
(-1-1j) - (-1+1j) = -2j
(-1-1j) * (-1+1j) = (2+0j)
---------------
Sample Input 3:
3-2j
1+4j

Sample Output 3:
(3-2j) + (1+4j) = (4+2j)
(3-2j) - (1+4j) = (2-6j)
(3-2j) * (1+4j) = (11+10j)
'''