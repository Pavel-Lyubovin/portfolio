# https://stepik.org/lesson/488831/step/2?thread=solutions&unit=480067
"""
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово
(или словосочетание). Например, английские слова evil и live – это анаграммы.
На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.
"""


def freq(s):
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1
    return d


s1, s2 = input().lower(), input().lower()
print(('NO', 'YES')[freq(s1) == freq(s2)])

'''
---------------
Sample Input 1:
thing
night

Sample Output 1:
YES

---------------
Sample Input 2:
cat
rat

Sample Output 2:
NO

---------------
Sample Input 3:
tea
eat

Sample Output 3:
YES
'''