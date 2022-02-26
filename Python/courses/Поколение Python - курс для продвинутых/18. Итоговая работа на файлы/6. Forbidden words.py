# https://stepik.org/lesson/448983/step/6
"""
Forbidden words
На вход программе подается строка текста с именем текстового файла.
Напишите программу, выводящую на экран содержимое этого файла,
но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).
Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
Гарантируется, что все слова в этом файле записаны в нижнем регистре.
"""


f_name = input()
with open(f_name) as f, open('forbidden_words.txt') as f_forb:
    forbs = f_forb.read().split()
    inp_txt = f.read()
    inp_txt_lower = inp_txt.lower()
    for forb in forbs:
        inp_txt_lower = inp_txt_lower.replace(forb.lower(), '*' * len(forb))
    for i, c in enumerate(inp_txt_lower):
        if c == '*':
            char = '*'
        else:
            char = inp_txt[i]
        print(char, end='')

'''
---------------
Sample Input 1
file1:
Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
file2(forbidden_words.txt):
hello email python the exam wor is

Sample Output 1:
*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!
'''