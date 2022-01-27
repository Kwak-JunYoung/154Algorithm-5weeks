s = input()
length = len(s)
arr = sorted([s[i:] for i in range(length)])
for a in arr:
    print(a)