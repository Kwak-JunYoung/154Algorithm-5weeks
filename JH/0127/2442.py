n = int(input())
s = 1
while(s < 2*n):
    for i in range(n-1, -1, -1): # 공백(i)   
        print(' '*i + '*'*s , end='')
        s += 2
        print()
    

## 다른 해설
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) +'*'*((2*i)-1))