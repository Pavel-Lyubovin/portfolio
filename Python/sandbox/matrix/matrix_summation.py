# Matrix summation: M1plusM2 = M1 + M2

n, m = map(int, input().split())
M1 = [[*map(int, input().split())] for i in range(n)]
_ = input()
M2 = [[*map(int, input().split())] for i in range(n)]
M1plusM2 = [[M1[i][j] + M2[i][j] for j in range(m)] for i in range(n)]
[print(*row) for row in M1plusM2]

'''
Sample Input 1:
2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3

Sample Output 1:
4 4 4 6
6 9 8 4

===============
Sample Input 2:
3 3
9 6 3
3 1 1
4 7 5

0 3 2
1 7 8
4 2 3

Sample Output 2:
9 9 5
4 8 9
8 9 8

===============
Sample Input 3:
1 1
1

1

Sample Output 3:
2
'''