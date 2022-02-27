import string
s = input()
a = string.ascii_lowercase
for i in range(len(a)):
    print(s.find(a[i]), end=" ")
