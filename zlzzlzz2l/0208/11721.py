word = list(input())

for i in range(0, len(word), 10):
    print(''.join(word[i:i+10]))