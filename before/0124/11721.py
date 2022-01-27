word = str(input())

while len(word):
    if len(word) >= 10:
        print(word[:10])
    else:
        print(word)
        break
    word = word[10:]