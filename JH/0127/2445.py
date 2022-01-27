n = int(input())

for i in range(1, n+1):
    # print('*'*i + ' '*(n-i) + ' '*(n-i) + '*'*i, end='')
    print('*'*i + ' '*2*(n-i) + '*'*i, end='') # 2배로 하는게 더 효율적
    print()
for i in range(n-1, 0, -1):
    print('*'*i + ' '*(n-i) + ' '*(n-i) + '*'*i, end='')
    print()
    