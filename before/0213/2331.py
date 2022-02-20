import math
a, p = list(map(int, input().split()))

d = [a]

while True:
    str_d = str(d[-1])
    a = sum([pow(int(letter), p) for letter in str_d])
    if a in d:
        print(d.index(a))
        break
    else:
        d.append(a)