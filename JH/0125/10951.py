# sys 사용
# import sys

# l = sys.stdin.readlines()

# for i in l:
#     a , b =  map(int, l.split())
#     print(a+b)
### runtime error

# EOFError 예외 처리
while 1:
    try:
        a ,b = map(int, input().split())
        print(a+b)
    except EOFError:
        break