# https://stepik.org/lesson/448983/step/5
"""
Tail of a File
На вход программе подается строка текста с именем текстового файла.
Напишите программу, выводящую на экран последние 10 строк данного файла.
"""


f_name = input()
with open(f_name) as f:
    buf = []
    for line in f:
        buf.append(line.rstrip())
        buf = buf[-10:]
    print(*buf, sep='\n')


'''
---------------
Sample Input 1 (in file):
there are many different holidays
on the first of january we
celebrate new year on the
seventh of january and the
twenty-fifth of december we
have christmas the twenty-third
of february is the day of the
defenders of the motherland
or the army day then comes
easter and radonitsa the
first of may is the labour
day the ninth of may is
victory day the third of july
is independence day then comes
the seventh of november the day
of the october revolution and so on

Sample Output 1:
of february is the day of the
defenders of the motherland
or the army day then comes
easter and radonitsa the
first of may is the labour
day the ninth of may is
victory day the third of july
is independence day then comes
the seventh of november the day
of the october revolution and so on
'''