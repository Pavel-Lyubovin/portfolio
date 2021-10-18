'''
Old key cellphone imitation.
The input message needs to be converted into sequences key pressing on old key cellphone.
Symbols missing from the cellphone keyboard should be skipped

===============
Sample Input 1:
The

Sample Output 1:
84433

===============
Sample Input 2:
Hello, World!

Sample Output 2:
4433555555666110966677755531111

===============
Sample Input 3:
He said: "I can solve this problem".

Sample Output 3:
44330777724443111110444022226607777666555888330844444777707777666225553361

===============
Sample Input 4:
Bee   Geek!!!

Sample Output 4:
2233330004333355111111111111
'''

message = input().upper()
keyboard = [' ', '.,?!:', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# Main coding dictionary: {' ': 0, '.': 1, ',': 11 ... }
d = {}
for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        d[keyboard[i][j]] = (j + 1) * str(i)
res = ''
for char in message:
    if char in d:
        res += d[char]
print(res)