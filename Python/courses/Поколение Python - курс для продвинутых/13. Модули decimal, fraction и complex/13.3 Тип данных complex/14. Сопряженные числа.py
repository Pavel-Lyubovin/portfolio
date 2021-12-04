# https://stepik.org/lesson/360942/step/14
"""
Дано натуральное число n и два комплексных числа z1, z2.
Напишите программу, которая вычисляет и выводит значение выражения:
z1 ** n  +  z2 ** n  +  z1_c ** n  +  z2_c ** (n + 1),
где z1_c и z2_c являются сопряженными числами для z1 и z2 соответственно.
"""


n, z1, z2 = int(input()), complex(input()), complex(input())
z1_c, z2_c = z1.conjugate(), z2.conjugate()  # Сопряженные комплексные числа
print(z1 ** n + z2 ** n + z1_c ** n + z2_c ** (n + 1))


'''
---------------
Sample Input 1:
1
2+3j
1+4j

Sample Output 1:
(-10-4j)
---------------
Sample Input 2:
2
2+3j
1+4j

Sample Output 2:
(-72+60j)
---------------
Sample Input 3:
3
1-1j
1+2j

Sample Output 3:
(-22+22j)
'''