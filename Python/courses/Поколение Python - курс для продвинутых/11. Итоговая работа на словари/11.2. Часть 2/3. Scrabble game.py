# https://stepik.org/lesson/492141/step/3
"""
В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв.
Чем реже буква встречается, тем больше она ценится:

Баллы 	Буква
1    	A, E, I, L, N, O, R, S, T, U
2 	    D, G
3 	    B, C, M, P
4 	    F, H, V, W, Y
5 	    K
8 	    J, X
10 	    Q, Z

Напишите программу подсчета итоговой стоимости введенного слова.
"""


s = input()
d = {
    "AEILNORSTU": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10
}
print(sum([v for char in s for k, v in d.items() if char in k]))


'''
---------------
Sample Input 1:
DANSER

Sample Output 1:
7

---------------
Sample Input 2:
FRESHENER

Sample Output 2:
15

---------------
Sample Input 3:
ZIP

Sample Output 3:
14
'''