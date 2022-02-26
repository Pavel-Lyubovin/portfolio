# https://stepik.org/lesson/511854/step/10
"""
Внутри шара
На вход программе подаются три строки текста с вещественными числами,
значениями абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства.
Напишите программу для проверки расположения всех точек с введенными координатами
внутри либо на поверхности шара с центром в начале координат и радиусом R = 2.
"""

abscissas = [float(x) for x in input().split()]
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))

dots = zip(abscissas, ordinates, applicates)

res = all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 2 ** 2, dots))

print(res)

'''
---------------
Sample Input 1:
0.0 1.0 2.0
0.0 0.0 1.1
0.0 1.0 1.5

Sample Output 1:
False
---------------
Sample Input 2:
0.0 0.0
1.5 0.0
1.1 1.1

Sample Output 2:
True
---------------
Sample Input 3:
0.637 -0.411 -0.247 1.658 0.061
-0.78 -1.374 0.762 0.306 -0.614
-1.317 -0.444 -0.572 -0.341 0.295

Sample Output 3:
True
'''
