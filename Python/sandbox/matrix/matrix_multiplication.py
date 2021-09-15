# Matrix multiplication: M1xM2 = M1 * M2

n1, m1 = map(int, input().split())
M1 = [[*map(int, input().split())] for _ in range(n1)]
_ = input()
n2, m2 = map(int, input().split())
M2 = [[*map(int, input().split())] for _ in range(n2)]
M1xM2 = [[sum([M1[i][k] * M2[k][j] for k in range(m1)]) for j in range(m2)] for i in range(n1)]
[print(*row) for row in M1xM2]

'''
Sample Input 1:
2 2
1 2
3 2

2 2
3 2
1 1

Sample Output 1:
5 4
11 8

===============
Sample Input 2:
3 2
2 5
6 7
1 8

2 3
1 2 1
0 1 0

Sample Output 2:
2 9 2
6 19 6
1 10 1

===============
Sample Input 3:
3 3
2 4 6
1 3 5
0 4 8

3 3
6 3 1
9 6 3
0 2 0

Sample Output 3:
48 42 14
33 31 10
36 40 12
'''