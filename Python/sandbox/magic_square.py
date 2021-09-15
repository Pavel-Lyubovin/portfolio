'''
Is a square matrix the magic square?
Magic square is the matrix of size n which meet conditions:
- has all numbers from 1 to n*n
- has equal element's sum in:
    - rows
    - columns
    - main diagonal
    - second diagonal
'''


n = int(input())
M = [[*map(int, input().split())] for _ in range(n)]

print(('NO', 'YES')[
          set(sum(M, [])) == set(range(1, n ** 2 + 1))  # numbers from 1 to n*n
            and
          len(set(map(sum, (
              *M,                               # all rows
              *zip(*M),                         # all columns
              [M[i][i] for i in range(n)],      # main diagonal
              [M[i][-i - 1] for i in range(n)]  # second diagonal
          ))) == 1)
      ])

'''
Sample Input 1:
3
8 1 6
3 5 7
4 9 2

Sample Output 1:
YES

--------------
Sample Input 2:
3
8 2 6
3 5 7
4 9 1

Sample Output 2:
NO

--------------
Sample Input 3:
3
4 9 2
3 5 7
8 1 6

Sample Output 3:
YES

--------------
Sample Input 4:
3
3 8 1
2 4 6
7 0 5

Sample Output 4:
NO
'''