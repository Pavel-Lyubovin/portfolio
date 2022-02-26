# https://stepik.org/lesson/530408/step/15
"""
CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
Напишите функцию read_csv для чтения данных из этого файла.
Она должна возвращать список словарей, интерпретируя первую строку как имена ключей,
а каждую последующую строку как значения этих ключей.
"""

def read_csv():
    with open('data.csv') as f:
        keys = f.readline().rstrip('\n').split(',')
        values = [line.rstrip('\n').split(',') for line in f]
    return [dict(zip(keys, val)) for val in values]


'''
---------------
Sample Input 1 (in file):
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21

Sample Output 1:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]
'''