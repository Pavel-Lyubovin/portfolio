'''
Morse code

===============
Sample Input 1:
Interstellar

Sample Output 1:
.. -. - . .-. ... - . .-.. .-.. .- .-.

===============
Sample Input 2:
SOS

Sample Output 2:
... --- ...

===============
Sample Input 3:
Agent 007

Sample Output 3:
.- --. . -. - ----- ----- --...
'''


message = input().upper()

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
morse_dict = dict(zip(letters, morse))  # {'A': '.-', 'B': '-...', 'C': '-.-.', ...
res = [morse_dict[char] for char in message if char in letters]
print(*res)
