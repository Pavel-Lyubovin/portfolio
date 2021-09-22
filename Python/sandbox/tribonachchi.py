# Generate Tribonachchi sequence

def tribonachchi(n):
    if n == 1:
        return (1,)
    elif n <= 3:
        return tribonachchi(n - 1) + (1,)
    else:
        t = tribonachchi(n - 1)
        return t + (t[-1] + t[-2] + t[-3], )


n = int(input())
print(*tribonachchi(n))

'''
---------------
Sample Input 1:
10

Sample Output 1:
1 1 1 3 5 9 17 31 57 105

---------------
Sample Input 2:
1

Sample Output 2:
1

---------------
Sample Input 3:
2

Sample Output 3:
1 1
---------------
'''


'''
Variant 'just output' (without saving sequence in tuple)
'''
# n = int(input())
# t1 = t2 = t3 = 1
# for _ in range(n):
#     print(t1, end=' ')
#     t1, t2, t3 = t2, t3, t1 + t2 + t3