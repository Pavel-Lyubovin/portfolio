# https://stepik.org/lesson/519126/step/12
"""
Загадка от Жака Фреско

Однажды Жака Фреско спросили:
"Если ты такой умный, почему не богатый?"
Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
"Были разноцветные козлы. Сколько?"
"Сколько чего?"
"Сколько из них составляет более 7% от общего количества козлов?"

Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS,
и далее непосредственно перечисление козлов разных цветов.
Перечень козлов включает только строки из первого списка.
Напишите программу создания файла answer.txt и вывода в него списка козлов,
которые удовлетворяют условию загадки от Жака Фреско.
"""

with open('goats.txt') as inp_f, open('answer.txt', 'w') as out_f:
    colours = {}
    for line in inp_f:
        if line == 'GOATS\n':
            break
    for line in inp_f:
        colours[line] = colours.get(line, 0) + 1
    total = sum(colours.values())
    res = list(filter(lambda x: colours[x] > (0.07 * total), colours.keys()))
    res = map(str.rstrip, res)
    print(*sorted(res), sep='\n', file=out_f)

'''
---------------
Sample Input 1 (in file):
COLOURS
Pink goat
Green goat
Black goat
GOATS
Pink goat
Pink goat
Black goat
Pink goat
Pink goat
Black goat
Green goat
Pink goat
Black goat
Black goat
Pink goat
Pink goat
Black goat
Black goat
Pink goat

Sample Output 1 (in file):
Black goat
Pink goat
'''