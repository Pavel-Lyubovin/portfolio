# Show moves for the chess khight

coord = input('Input start position (for example d2): ')
col = ord(coord[0]) - ord('a')
row = 8 - int(coord[1])

board = [['.'] * 8 for _ in range(8)]
board[row][col] = 'N'

for i in range(max(0, row - 2), min(8, row + 3)):
    for j in range(max(0, col - 2), min(8, col + 3)):
        if abs((row - i) * (col - j)) == 2:
            board[i][j] = '*'

[print(*row) for row in board]

'''
Sample Input 1:
b6

Sample Output 1:
* . * . . . . .
. . . * . . . .
. N . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .


Sample Input 2:
f3

Sample Output 2:
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . * . * .
. . . * . . . *
. . . . . N . .
. . . * . . . *
. . . . * . * .
'''