'''
ОПИСАНИЕ ЗАДАЧИ:

Написать программу на питоне, выдающую без повторений на stdout
все различные перестановки N одинаковых (0) и N разных чисел (от 1 до N).
Запуск программы должен выглядеть так: "python permute.py 5"
Скажем, для N=5, пусть это будут числа 0 0 0 0 0 1 2 3 4 5 .
Примеры таких перестановок: 0000012345 или 5012034000
Теперь выведите все такие перестановки для N=5 и сохраните их в файл.
Посчитайте с помощью wc количество строк в этом файле.
Сколько получилось?
Попробуйте оценить время, которое будет ваш алгоритм считаться для N=7
(это не значит, что ваш алгоритм должен быть самый лучший и быстрый,
просто грубо оцените примерное время выполнения именно для вашего алгоритма,
исходя из вашего понимания).
'''

'''
ОТВЕТЫ:
1. Получилось 30240 строк (для этого надо запустить программу, код которой ниже)
Это число можно получить аналитически: количество перестановок в данном случае
равняется 10! / 5! = 6 * 7 * 8 * 9 * 10 = 30240
2. Для N==7 количество перестановок составит 14! / 7!.
Соответственно алгоритм будет работать примерно в (14! / 7!) * (5! / 10!) раз дольше.
Если упростить, то получим (11 * 12 * 13 * 14) / (6 * 7) = в 572 раза медленнее.
Мой алгоритм при N==5 отработал за 1,06 секунды. Значит при N==7 время работы составит
1,06 * 572 = 606,32 сек или примерно 10 минут.
'''

from sys import argv
from itertools import permutations

_, N = argv
N = int(N)

stuff = [i for i in range(1, N + 1)]
stuff.extend([0] * N)

res = set()
for subset in permutations(stuff, N * 2):
    res.add(subset)

with open('result.txt', 'w') as f:
    for row in sorted(res):
        f.write(''.join([str(i) for i in row]) + '\n')