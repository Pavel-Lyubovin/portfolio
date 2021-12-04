# https://stepik.org/lesson/488831/step/7
"""
Напишите программу для расшифровки секретного слова методом частотного анализа.
"""


encrypted = decrypted = input()
d = {}
for _ in range(int(input())):
    char, freq = input().split(': ')
    d[int(freq)] = char
for char in set(encrypted):
    freq = encrypted.count(char)
    decrypted = decrypted.replace(char, d[freq])
print(decrypted)


'''
---------------
Sample Input 1:
*!*!*?
3
а: 3
н: 2
с: 1

Sample Output 1:
ананас

---------------
Sample Input 2:
pop
2
д: 2
е: 1

Sample Output 2:
дед
'''