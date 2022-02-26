# https://stepik.org/lesson/448983/step/4
"""
Самое длинное слово в файле
Вам доступен текстовый файл words.txt со словами, разделенными пробелом.
Напишите программу, которая находит и выводит самые длинные слова этого файла,
не меняя порядка их следования.
"""


with open('words.txt') as f:
    words = f.read().split()
    max_l = len(max(words, key=len))
    [print(word) for word in words if len(word) == max_l]


'''
---------------
Sample Input 1 (in file):
there are many different holidays on the first of january we celebrate new year on the seventh of january and the twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the motherland or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may is victory day the third of july is independence day then comes the seventh of november the day of the october revolution and so on

Sample Output 1:
twenty-fifth
twenty-third
independence
'''