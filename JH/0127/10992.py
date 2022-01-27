n = int(input())
# cen = 1 # 별 사이에 공백 수

# print(' '*(n-1)+'*') # 맨 위층
# for i in range(n-2, 0, -1): # 앞 공백
#     print(' '*i + '*' + ' '*cen + '*',end='')
#     cen += 2
#     print()
# print('*'*(2*n -1)) # 맨 아래층

# ###맞왜틀?????????


for i in range(1, n+1):
    if i == 1:
        print(' '*(n-i) + '*', end='')
    elif i == n :
        print('*'* (2*i -1))
    else: 
        print(' '*(n-i) + '*' + ' '*(2*i -3) + '*', end='')
    print()
