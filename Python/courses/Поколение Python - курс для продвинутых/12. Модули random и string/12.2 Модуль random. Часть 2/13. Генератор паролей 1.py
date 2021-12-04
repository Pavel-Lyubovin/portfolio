# https://stepik.org/lesson/356380/step/13
"""
Напишите программу, которая с помощью модуля random генерирует nnn паролей длиной mmm символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (большая и маленькая буквы);
    «0» (цифра).
"""


import random
import string

n, m = int(input()), int(input())
chars = ''.join(char for char in string.ascii_letters + string.digits if char not in 'lI1oO0')
for i in range(n):
    pswd = ''.join([chars[random.randrange(len(chars))] for _ in range(m)])
    print(pswd)


'''
---------------
Sample Input 1:
9
7

Sample Output 1:
YbykdW8
heEWSyL
MDxYCzf
syWRujr
mFGBYNJ
bhmg5ip
2XmPgsx
hy7UMVs
JzKPyBw
---------------
Sample Input 2:
3
15

Sample Output 2:
itnSA8L3UsBXhWb
82hvi7yFBWjw6fg
hSd6V3CxyHvgw2m
---------------
Sample Input 3:
20
4

Sample Output 3:
QcLR
d8Xj
85dQ
aXr4
cuVj
38Dx
sd4Q
bkrA
tb96
p6Gg
neVN
AvQJ
4fzr
X68L
Lwxr
j8gQ
aR5Q
QCq4
a9Qm
Az4M
'''