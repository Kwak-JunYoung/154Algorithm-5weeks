alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = str(input())
for a in alphabet:
    if a in s:
        print(s.index(a), end = ' ')
    else:
        print(-1, end = ' ')