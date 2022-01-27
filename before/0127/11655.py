import sys
sent = sys.stdin.readline()

newSent = ''
for letter in sent:
    if letter.islower():
        newSent += chr((ord(letter) - 97 + 13) % 26 + 97)
    elif letter.isupper():
        newSent += chr((ord(letter) - 65 + 13) % 26 + 65)
    elif letter != '\n':
        newSent += letter
print(newSent)