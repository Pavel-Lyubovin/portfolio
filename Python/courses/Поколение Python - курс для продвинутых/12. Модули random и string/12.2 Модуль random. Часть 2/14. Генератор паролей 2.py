# https://stepik.org/lesson/356380/step/14
"""
Напишите программу, которая с помощью модуля random генерирует nnn паролей длиной mmm символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (большая и маленькая буквы);
    «0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать
хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.
"""


import random
import string


up_chars = ''.join(char for char in string.ascii_uppercase if char not in 'IO')
low_chars = ''.join(char for char in string.ascii_lowercase if char not in 'lo')
digits = ''.join(char for char in string.digits if char not in '10')
chars = up_chars + low_chars + digits


def generate_password(length):
    password = [random.choice(i) for i in (up_chars, low_chars, digits)] \
                + [chars[random.randrange(len(chars))] for _ in range(length - 3)]
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
passwords = generate_passwords(n, m)
print(*passwords, sep='\n')


'''
---------------
Sample Input 1:
9
7

Sample Output 1:
iHnPg7q
Njj9m3N
tQ9v5ut
6qPZ3tV
6gVScya
kU8ncAY
5CKX9Da
UTQRve4
FyRe8NN
---------------
Sample Input 2:
15
3

Sample Output 2:
7qB
4Wp
r2V
Zq3
Y5q
iL3
M9v
7Hy
8tW
5Jz
a4K
3Kt
cN6
7Tk
Pg5
---------------
Sample Input 3:
20
4

Sample Output 3:
4buF
Ci32
4zXK
p3By
pQs9
aP8n
7tGb
QV2e
98Eu
8BbG
R9sr
c8Uv
tt4H
66Cq
J8mW
kCm8
k8PH
7EWp
DH4q
E5wF
'''