# https://stepik.org/lesson/488831/step/6
"""
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу,
которая поможет Тимуру находить все номера определённого друга.
"""


tel_book = {}
for _ in range(int(input())):
    tel, name = input().split()
    tel_book.setdefault(name.lower(), []).append(tel)
for _ in range(int(input())):
    name = input().lower()
    print(*tel_book[name] if name in tel_book else ['абонент не найден'])


'''
---------------
Sample Input:
3
79184219577 Женя
79194249271 Руслан
79281234567 Женя
3
Руслан
женя
Рустам

Sample Output:
79194249271
79184219577 79281234567
абонент не найден
'''