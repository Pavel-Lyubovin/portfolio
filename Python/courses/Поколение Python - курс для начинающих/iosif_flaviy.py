# n soldiers (from 1 to n) stood in a circle
# and kill every k soldier starting from the first soldier
# The last soldier will survive
# Who of them will survive?
# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F
n, k = int(input()), int(input())

soldiers = [i + 1 for i in range(n)]


def kill(idx, k):
    idx = (idx + k - 1) % len(soldiers)
    del soldiers[idx]
    return idx


idx = 0
while len(soldiers) > 1:
    idx = kill(idx, k)

print(soldiers[0])


'''
Sample Input 1:
2
1
Sample Output 1:
2

Sample Input 2:
5
2
Sample Output 2:
3

Sample Input 3:
7
5
Sample Output 3:
6
'''


