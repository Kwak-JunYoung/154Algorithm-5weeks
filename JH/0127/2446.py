n = int(input())
s = 2*n -1
s2 = 3
for i in range(n): # 공백 (i)
    print(' '*i + '*'*s, end='')
    s -= 2
    print()
for i in range(n-2, -1, -1): 
    print(' '*i + '*'*s2, end='')
    s2 += 2
    print()

## 다른 풀이
n = int(input())
for i in range(n):
    print(" " * i + "*" * ((n - i) * 2 - 1))
for i in range(n - 2, -1, -1):
    print(" " * i + "*" * ((n - i) * 2 - 1))