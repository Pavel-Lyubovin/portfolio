'''
TASK DESCRIPTION:

Use English SpaCy lib, find all tokens with only digits
and all proper nouns (PROPN, aka, personal nouns ) in the text,
count it and output it right-aligned in the HTML.
For example, for the text "we need 2 tickets to Dublin, and 1/2 a spoon of milk"
read from the stdin (use python myprogram.py < input.txt >output.html )
the program should output that "2" was found twice (output "2"),
"1" was found once (output "1"), "Dublin" was found once (output "1").
'''

import spacy, re


phrase = input()  # for example: we need 2 tickets to Dublin, and 1/2 a spoon of milk
nlp = spacy.load('en_core_web_sm')
doc = nlp(phrase)

res = dict()
for token in doc:
    if token.pos_ == 'PROPN':
        res[token.text] = res.get(token.text, 0) + 1
    elif token.pos_ == 'NUM':
        nums = re.findall(r'\d+', token.text)
        for num in nums:
            res[num] = res.get(num, 0) + 1

output = '<html><body><p align="right">'
for key, value in res.items():
    output += key + ' ' + str(value) + '<br>'
output += '</p></body></html>'

print(output)


'''
Install notes:
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_sm
'''

'''
https://github.com/explosion/spaCy/issues/4756
instruction how install en_core_web_sm into venv:
----------- for example:
source /home/disha/Desktop/project/python/parser/venv/bin/activate
pip install -U spacy
spacy download en_core_web_sm
'''