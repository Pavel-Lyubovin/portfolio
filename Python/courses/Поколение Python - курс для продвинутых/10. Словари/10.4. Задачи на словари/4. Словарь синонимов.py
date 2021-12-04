# https://stepik.org/lesson/488831/step/4
"""
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу,
которая для одного данного слова определяет его синоним.
"""


n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = value
    d[value] = key

query = input()
print(d[query])

'''
---------------
Sample Input 1:
4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty

Sample Output 1:
Beautiful

---------------
Sample Input 2:
3
Kind Affable
Intellect Mind
Popular Celebrated
Popular

Sample Output 2:
Celebrated
'''