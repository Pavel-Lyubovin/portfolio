# https://stepik.org/lesson/488831/step/3
"""
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
"""


def char_freq(s):
    d = {}
    for char in s:
        if char.isalpha():
            d[char] = d.get(char, 0) + 1
    return d


s1, s2 = input().lower(), input().lower()
print(('NO', 'YES')[char_freq(s1) == char_freq(s2)])

'''
---------------
Sample Input 1:
Вижу зверей
Живу резвей

Sample Output 1:
YES

---------------
Sample Input 2:
Когда увидимся
тогда и свидимся

Sample Output 2:
NO

---------------
Sample Input 3:
С мая весной
сам я не свой

Sample Output 3:
YES
'''