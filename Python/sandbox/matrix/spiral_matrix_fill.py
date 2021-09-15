# Spiral matrix fill

n, m = map(int, input().split())
M = [[0] * m for _ in range(n)]
i, j, di, dj = 0, 0, 0, 1
for num in range(1, n * m + 1):
    M[i][j] = num
    if M[(i + di) % n][(j + dj) % m]:
        di, dj = dj, -di  # change direction
    i += di
    j += dj
[print(*[str(el).ljust(3) for el in row], sep='') for row in M]


'''
Sample Input 1:
4 5

Sample Output 1:
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8

===============
Sample Input 2:
1 6

Sample Output 2:
1  2  3  4  5  6

===============
Sample Input 3:
3 3

Sample Output 3:
1  2  3
8  9  4
7  6  5
'''