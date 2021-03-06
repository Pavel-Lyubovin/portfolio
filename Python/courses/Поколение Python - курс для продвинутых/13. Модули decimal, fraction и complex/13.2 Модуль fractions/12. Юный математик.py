# https://stepik.org/lesson/362369/step/12
"""
Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем.
Вчера на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя,
и несократимой, если нет равной ей дроби с меньшими натуральными числителем и знаменателем.

Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки
с правильными несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число nnn. Напишите программу,
которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n.
"""

from fractions import Fraction as F

n = int(input())
numerator = n // 2
denominator = n - numerator
d = F(numerator, denominator)
while d.numerator != numerator:
    numerator -= 1
    denominator += 1
    d = F(numerator, denominator)
print(d)


'''
---------------
Sample Input 1:
10

Sample Output 1:
3/7
---------------
Sample Input 2:
23

Sample Output 2:
11/12
---------------
Sample Input 3:
3

Sample Output 3:
1/2
'''