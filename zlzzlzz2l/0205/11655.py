word = list(input())

for i in range(len(word)):
    if word[i].isdigit():
        continue
    if word[i].isspace():
        continue

    ch = ord(word[i])

    if ch >= 65 and ch <= 90:
        ch += 13
        if ch > 90:
            ch -= 90
            ch = 64 + ch
    elif ch >= 97 and ch <= 122:
        ch += 13
        if ch > 122:
            ch -= 122
            ch = 96 + ch

    ans = chr(ch)
    word[i] = ans

print(''.join(word))