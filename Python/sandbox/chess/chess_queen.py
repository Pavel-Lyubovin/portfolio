# # Show moves for the chess queen
coord = input('Input start position (for example d2): ')
col = ord(coord[0]) - ord('a')
row = 8 - int(coord[1])
board = [['Q' if i == row and j == col \
              else '*' if i == row or j == col or abs(i - row) == abs(j - col) \
              else '.' for j in range(8)] for i in range(8)]
[print(*row) for row in board]

'''
Sample Input 1:
c4

Sample Output 1:
. . * . . . * .
. . * . . * . .
* . * . * . . .
. * * * . . . .
* * Q * * * * *
. * * * . . . .
* . * . * . . .
. . * . . * . .

===============
Sample Input 2:
a1

Sample Output 2:
* . . . . . . *
* . . . . . * .
* . . . . * . .
* . . . * . . .
* . . * . . . .
* . * . . . . .
* * . . . . . .
Q * * * * * * *

===============
Sample Input 3:
h5

Sample Output 3:
. . . . * . . *
. . . . . * . *
. . . . . . * *
* * * * * * * Q
. . . . . . * *
. . . . . * . *
. . . . * . . *
. . . * . . . *
'''