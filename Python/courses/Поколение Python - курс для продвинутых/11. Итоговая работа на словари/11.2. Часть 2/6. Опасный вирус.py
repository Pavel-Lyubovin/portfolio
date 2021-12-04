# https://stepik.org/lesson/492141/step/6
"""
В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус
и сломал контроль прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

    запись W (write, доступ на запись в файл);
    чтение R (read, доступ на чтение из файла);
    запуск X (execute, запуск на исполнение файла).

Напишите программу для восстановления контроля прав доступа к файлам.
Ваша программа для каждого запроса должна будет возвращать OK если выполняется допустимая операция, и Access denied,
если операция недопустима.
"""


d = {}
for _ in range(int(input())):
    file_name, *rules, = input().split()
    d[file_name] = rules

translate = {'write': 'W', 'read': 'R', 'execute': 'X'}
for _ in range(int(input())):
    command, file_name = input().split()
    print(('Access denied', 'OK')[translate[command] in d[file_name]])


'''
---------------
Sample Input 1:
5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe

Sample Output 1:
Access denied
Access denied
OK
OK
OK
OK
---------------
Sample Input 2:
2
marvel_movies X
dc_com X R
2
execute dc_com
write dc_com

Sample Output 2:
OK
Access denied
'''