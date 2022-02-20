# n = int(input())
import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    order = sys.stdin.readline().strip()

    if order.startswith('push'): ### startsswith : 특정문자로 시작하는경우
        s , x = order.split()
        stack.append(int(x))
    elif order == 'pop':
        if bool(stack):
            v = stack.pop()
            print(v)
        else:
             print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(int(not bool(stack)))
    elif order == "top":
        if bool(stack):
            print(stack[-1])
        else: 
            print(-1)
            
### 시간초과
'''
input() --> sys.stdin.readline() 해결됨

9줄에서 .strip() 안붙이면 공백도 포함되서 틀렸다 나옴!! (주의**)


'''
