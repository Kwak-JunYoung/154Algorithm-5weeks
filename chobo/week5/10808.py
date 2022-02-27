import string
rst = [0 for _ in range(26)]
w = input()
a = string.ascii_lowercase
for i in range(len(w)):
    for j in range(len(a)):
        if w[i] == a[j]:
            rst[j] = rst[j] + 1

for i in range(len(a)):
    print(rst[i], end=" ")
