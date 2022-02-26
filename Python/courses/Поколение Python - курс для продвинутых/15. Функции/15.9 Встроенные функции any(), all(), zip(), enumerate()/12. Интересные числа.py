# https://stepik.org/lesson/511854/step/12
"""
Интересные числа
На вход программе подаются два натуральных числа a и b.
Напишите программу с использованием встроенной функции all()
для обнаружения всех целых чисел в диапазоне [a;b],
которые делятся на каждую содержащуюся в них цифру без остатка.
"""

a, b = int(input()), int(input())
res = []
for num in range(a, b + 1):
    if all(map(lambda x: int(x) > 0 and num % int(x) == 0, str(num))):
        res.append(num)
print(*res)

'''
---------------
Sample Input 1:
1
25

Sample Output 1:
1 2 3 4 5 6 7 8 9 11 12 15 22 24
---------------
Sample Input 2:
20
30

Sample Output 2:
22 24
---------------
Sample Input 3:
50
150

Sample Output 3:
55 66 77 88 99 111 112 115 122 124 126 128 132 135 144
'''
