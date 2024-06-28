# Diagonal matrix fill

n, m = map(int, input().split())
M = [['.'] * m for i in range(n)]
num = 0
for diag_n in range(n + m - 1):
    for i in range(max(0, diag_n - m + 1), min(diag_n + 1, n)):
        num += 1
        M[i][diag_n - i] = num
[print(*[str(el).ljust(3) for el in row]) for row in M]

'''
Sample Input 1:
3 5

Sample Output 1:
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15

==============
Sample Input 2:
3 4

Sample Output 2:
1  2  4  7
3  5  8  10
6  9  11 12

==============
Sample Input 3:
2 2

Sample Output 3:
1  2
3  4

==============
Sample Input 4:
8 1

Sample Output 4:
1
2
3
4
5
6
7
8

==============
Sample Input 5:
8 2

Sample Output 5:
1  2
3  4
5  6
7  8
9  10
11 12
13 14
15 16

'''