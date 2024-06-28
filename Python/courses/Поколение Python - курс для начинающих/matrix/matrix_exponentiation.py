# Matrix exponentiation: Mexp_m = M ** m

n = int(input())
M = [[*map(int, input().split())] for _ in range(n)]
m = int(input())
Mexp_m = M.copy()
for _ in range(m - 1):
    Mexp_m = [[sum([Mexp_m[i][k] * M[k][j] for k in range(n)]) for j in range(n)] for i in range(n)]
[print(*row) for row in Mexp_m]

'''
Sample Input 1:
3
1 2 3
4 5 6
7 8 9
2

Sample Output 1:
30 36 42
66 81 96
102 126 150

===============
Sample Input 2:
3
1 2 1
3 3 3
1 2 1
5

Sample Output 2:
1666 2222 1666
3333 4443 3333
1666 2222 1666

===============
Sample Input 3:
5
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3

Sample Output 3:
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
'''